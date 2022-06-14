#!/usr/bin/python3
from ypstruct import structure
import numpy as np
import matplotlib.pyplot as plt
from ypstruct import structure
import math

F = 2722
E = 200e9  # YOUNGS MODULUS OF BEAM
G = 75.8e9  # SHEAR MODULUS OF BEAM
L = 0.3556  # lENGHT
alpha = 0.9
tau_max = 0.09e9  # MAXIMUM ALLOWED SHEAR STRESS
sigma_max = 0.2e9  # MAXIMUM ALLOWED BENDING STRESS
delta_max = 0.0065  # MAXIMUM ALLOWED TIP DEFLECTION
real_deflex = []
real_cost = []
real_total = []


def cost_fixed(x):
    return (67413 * (x[0] ** 2) * x[1]) + (2935 * x[2] * x[3] * (L + x[1]))


def deflex_fixed(x):
    return (4 * F * (L ** 3)) / (E * x[3] * (x[2] ** 3))


def total_fixed(x):
    return 0.5 * deflex_fixed(x) + 0.5 * cost_fixed(x)


def run(problem, params):
    # Problem info
    costfunc = problem.costfunc
    nvar = problem.nvar
    varmin = problem.varmin
    varmax = problem.varmax

    # Params info
    maxit = params.maxit
    npop = params.npop
    pc = params.pc
    nc = int(round(npop / 2) * 2)
    mu = params.mu
    sigma = params.sigma
    beta = params.beta
    ninc = params.ninc

    # Empty Individual Template
    empty_individual = structure()
    empty_individual.position = None
    empty_individual.cost = None

    # Best Solution Found
    bestsol = empty_individual.deepcopy()
    bestsol.cost = 100000

    # Initialize Population
    pop = empty_individual.repeat(npop)
    for i in range(0, npop):
        pop[i].position = np.random.uniform(varmin, varmax, nvar)
        pop[i].cost = costfunc(pop[i].position)
        if pop[i].cost < bestsol.cost:
            bestsol = pop[i].deepcopy()

    # Best cost of iterations
    bestcost = np.empty(maxit)
    # it = 0

    # Main loop
    for it in range(maxit):

        costs = [x.cost for x in pop]
        avg_cost = np.mean(costs)

        if avg_cost != 0:
            costs = avg_cost / costs
        probs = np.exp(-beta * costs)

        # while ninc != 0:
        pop_child = []
        for _ in range(nc // 2):
            # # Select Parents
            # q = np.random.permutation(npop)
            # p1 = pop[q[0]]
            # p2 = pop[q[1]]

            # Select with roulette_wheel_selection
            p1 = pop[roulette_wheel_selection(probs)]
            p2 = pop[roulette_wheel_selection(probs)]

            # Perform Crossover
            c1, c2 = crossover(p1, p2)

            # Perform Mutation
            c1 = mutation(c1, mu, sigma)
            c2 = mutation(c2, mu, sigma)

            # Bounds
            apply_bound(c1, varmin, varmax)
            apply_bound(c2, varmin, varmax)

            # Evaluate
            c1.cost = costfunc(c1.position)
            if c1.cost < bestsol.cost:
                bestsol = c1.deepcopy()

            c2.cost = costfunc(c2.position)
            if c2.cost < bestsol.cost:
                bestsol = c2.deepcopy()

            # Add to population
            pop_child.append(c1)
            pop_child.append(c2)

        # Merge, Sort ans select
        pop += pop_child
        pop = sorted(pop, key=lambda x: x.cost)
        pop = pop[0:npop]

        # Store best cost
        bestcost[it] = bestsol.cost
        # it+=1
        print(f'Iteration {it}: Best Cost = {bestcost[it]}')
        print(bestsol.position)
        real_cost.append(cost_fixed(pop[0].position))
        real_deflex.append(deflex_fixed(pop[0].position))
        real_total.append(total_fixed(pop[0].position))

        it += 1
        if it == (maxit-1):
            print(bestsol.position)
            print(cost_fixed(pop[0].position))
            print(deflex_fixed(pop[0].position))
    out = structure()
    out.pop = pop
    out.bestsol = bestsol
    out.bestcost = bestcost
    return out


def crossover(p1, p2):
    c1 = p1.deepcopy()
    c2 = p2.deepcopy()
    gamma = 0.1
    alpha = np.random.uniform(-gamma, 1 + gamma, *c1.position.shape)
    c1.position = alpha * p1.position + (1 - alpha) * p2.position
    c2.position = alpha * p2.position + (1 - alpha) * p1.position

    return c1, c2


def mutation(x, mu, sigma):
    y = x.deepcopy()
    flag = np.random.rand(*x.position.shape) <= mu
    ind = np.argwhere(flag)
    y.position[ind] += sigma * np.random.randn(*ind.shape)
    return y


def apply_bound(x, varmin, varmax):
    x.position = np.maximum(x.position, varmin)
    x.position = np.minimum(x.position, varmax)


def roulette_wheel_selection(p):
    c = np.cumsum(p)
    r = sum(p) * np.random.rand()
    ind = np.argwhere(r <= c)
    return ind[0][0]


def Moment(x):  # BENDING MOMENT AT WELD POINT
    return F * (L + x[1] / 2)


def R(x):  # CONSTANT
    return np.sqrt((x[1] ** 2) / 4 + ((x[0] + x[2]) / 2) ** 2)


def J(x):  # POLAR MOMENT OF INERTIA
    return 2 * (np.sqrt(2) * x[0] * x[1] * ((x[1] ** 2) / 12 + ((x[0] + x[2]) / 2) ** 2))


def sigma(x):  # BENDING STRESS
    return (6 * F * L) / (x[3] * x[2] ** 2)


def delta(x):  # TIP DEFLECTION
    return (4 * F * L ** 3) / (E * x[3] * x[2] ** 3)


def F_buckling(x):  # BUCKLING LOAD
    return 4.013 * E * np.sqrt((x[2] ** 2 * x[3] ** 6) / 36) * (1 - x[2] * np.sqrt(E / (4 * G)) / (2 * L)) / (L ** 2)


def tau_1D(x):  # 1ST DERIVATIVE OF SHEAR STRESS
    return F / (np.sqrt(2) * x[0] * x[1])


def tau_2D(x):  # 2ND DERIVATIVE OF SHEAR STRESS
    return (Moment(x) * R(x)) / J(x)


def tau(x):  # SHEAR STRESS
    return np.sqrt(tau_1D(x) ** 2 + 2 * tau_1D(x) * tau_2D(x) * x[1] / (2 * R(x)) + tau_2D(x) ** 2)


def G1(x):
    return tau(x) <= tau_max  # MAX SHEAR STRESS CONSTRAINT


def G2(x):
    return sigma(x) <= sigma_max  # MAX BENDING STRESS CONSTRAINT


def G3(x):
    return F_buckling(x) >= F  # BUCKLING LOAD CONSTRAINT


def G4(x):
    return delta(x) <= delta_max  # MAX TIP DEFLECTION CONSTRAINT


def G5(x):
    return x[0] <= x[3]


# def G1(x):
#     # MAX SHEAR STRESS CONSTRAINT
#     if tau(x) > tau_max:
#         # print(tau(x))
#         return tau(x) / tau_max
#     else:
#         return 0
#
#
# def G2(x):
#     # MAX BENDING STRESS CONSTRAINT
#     if sigma(x) > sigma_max:
#         # print(sigma(x))
#         return sigma(x) / sigma_max
#     else:
#         return 0
#
#
# def G3(x):
#     # BUCKLING LOAD CONSTRAINT
#     if F_buckling(x) > F:
#         return F_buckling(x) / F
#     else:
#         return 0
#
#
# def G4(x):
#     # MAX TIP DEFLECTION CONSTRAINT
#     if delta(x) > delta_max:
#         # print('hi')
#         # print(delta(x))
#         return delta(x) / delta_max
#     else:
#         return 0
#
#
# def G5(x):
#     # WELD COVERAGE CONSTRAINT
#     if x[0] > x[3]:
#         return x[0] / x[3]
#     else:
#         return 0
#
#
def costfunction(x):
    f_cost = ((67413 * (x[0] ** 2) * x[1]) + (2935 * x[2] * x[3] * (L + x[1]))) / 0.010133960800000001
    f_deflex = (4 * F * (L ** 3)) / (E * x[3] * (x[2] ** 3)) / 1.1762469291338585e-06

    validade1 = G1(x)
    validade2 = G2(x)
    validade3 = G3(x)
    validade4 = G4(x)
    validade5 = G5(x)
    # restriction = sum([G1(x), G2(x), G3(x), G4(x), G5(x)])  # ,G6(x),G7(x)]
    # print(restriction)
    # penalty = (5 - restriction) * 100000
    if not validade1:
        g1 = tau(x) / tau_max
        # print('valido1')
    else:
        g1 = 0

    if not validade2:
        g2 = sigma(x) / sigma_max
        # print('valido2')

    else:
        g2 = 0

    if not validade3:
        g3 = F_buckling(x) / F
        # print('valido3')

    else:
        g3 = 0

    if not validade4:
        g4 = delta(x) / delta_max
        # print('valido4')

    else:
        g4 = 0

    if not validade5:
        g5 = x[0] / x[3]
        # print('validade')
    else:
        g5 = 0

    penal = g1 + g2 + g3 + g4 + g5
    return (alpha * f_cost + (1 - alpha) * f_deflex) + 10 * penal


# Problem Defining
problem = structure()
problem.costfunc = costfunction
problem.nvar = 4
problem.varmin = [0.0032, 0.0025, 0.0025, 0.0032]
problem.varmax = [0.127, 0.254, 0.254, 0.127]

# Parameters Genetic Algorithm
params = structure()
params.maxit = 200
params.npop = 10
params.pc = 1
params.mu = 0.1
params.sigma = 0.1
params.beta = 1
# params.ninc = ninc
# Run GA
out = run(problem, params)


# print('prints')
# print('this is final deflex')
# print(real_deflex)
# print('this is final cost')
# print(real_cost)
# print('this is best cost')
# print(out.bestcost)
# Results
plt.plot(out.bestcost)
# plt.plot(real_total)

plt.xlim(0, params.maxit)
plt.xlabel('Iterations')
plt.ylabel('Best Cost')
plt.title('Genetic Algorithm (GA)')
plt.grid(True)
plt.show()
