#!/usr/bin/python3

import numpy as np
import random
import math

F = 2722
E = 200e9  # YOUNGS MODULUS OF BEAM
G = 75.8e9  # SHEAR MODULUS OF BEAM
L = 0.3556  # lENGHT
# alpha = 0.5
tau_max = 0.09e9  # MAXIMUM ALLOWED SHEAR STRESS
sigma_max = 0.2e9  # MAXIMUM ALLOWED BENDING STRESS
delta_max = 0.0065  # MAXIMUM ALLOWED TIP DEFLECTION


def cost_fixed(x):
    return (67413 * (x[0] ** 2) * x[1]) + (2935 * x[2] * x[3] * (L + x[1]))


def deflex_fixed(x):
    return (4 * F * (L ** 3)) / (E * x[3] * (x[2] ** 3))


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


def objetctive_function(pop, alpha):
    fitness = np.zeros(pop.shape[0])
    for i in range(pop.shape[0]):
        x = pop[i]
        f_cost = ((67413 * (x[0] ** 2) * x[1]) + (2935 * x[2] * x[3] * (L + x[1]))) / 0.010133960800000001
        f_deflex = (4 * F * (L ** 3)) / (E * x[3] * (x[2] ** 3)) / 1.1762469291338585e-06

        validade1 = G1(x)
        validade2 = G2(x)
        validade3 = G3(x)
        validade4 = G4(x)
        validade5 = G5(x)

        if not validade1:
            g1 = tau(x) / tau_max
        else:
            g1 = 0

        if not validade2:
            g2 = sigma(x) / sigma_max

        else:
            g2 = 0

        if not validade3:
            g3 = F_buckling(x) / F

        else:
            g3 = 0

        if not validade4:
            g4 = delta(x) / delta_max

        else:
            g4 = 0

        if not validade5:
            g5 = x[0] / x[3]
        else:
            g5 = 0

        penal = g1 + g2 + g3 + g4 + g5
        fitness[i] = (alpha * f_cost + (1 - alpha) * f_deflex) + 5 * penal
        # A = 10
        # fitness[i] = 10e6 - (A*2 + x[0]**2 - A * np.cos(2 * math.pi * x[0]) + x[1] ** 2 - A * np.cos(2 * math.pi * x[1]))

        # fitness[i] = 0.4 / (1 + 0.02 * ((x[0] - (-20)) ** 2 + (x[1] - (-20)) ** 2)) \
        #              + 0.2 / (1 + 0.5 * ((x[0] - (-5)) ** 2 + (x[1] - (-25)) ** 2)) \
        #              + 0.7 / (1 + 0.01 * ((x[0] - (0)) ** 2 + (x[1] - 30) ** 2)) \
        #              + 1 / (1 + 2 * ((x[0] - 30) ** 2 + (x[1] - 0) ** 2)) \
        #              + 0.05 / (1 + 0.1 * ((x[0] - 30) ** 2 + (x[1] - (-30)) ** 2))

    return fitness


def selection(pop, fitness, pop_size):
    next_generation = np.zeros((pop_size, pop.shape[1]))
    elite = np.argmin(fitness)
    next_generation[0] = pop[elite]
    fitness = np.delete(fitness, elite)
    # print(fitness)
    pop = np.delete(pop, elite, axis=0)
    P = [f / sum(fitness) for f in fitness]
    index = list(range(pop.shape[0]))
    index_selected = np.random.choice(index, size=pop_size - 1, replace=False, p=P)
    s = 0
    for j in range(pop_size - 1):
        next_generation[j + 1] = pop[index_selected[s]]
        s += 1
    return next_generation


def crossover(pop, crossover_rate):
    offspring = np.zeros((crossover_rate, pop.shape[1]))
    for i in range(int(crossover_rate / 2)):
        r1 = random.randint(0, pop.shape[0] - 1)
        r2 = random.randint(0, pop.shape[0] - 1)
        while r1 == r2:
            r1 = random.randint(0, pop.shape[0] - 1)
            r2 = random.randint(0, pop.shape[0] - 1)
        cutting_point = random.randint(0, pop.shape[1] - 1)
        offspring[2 * i, 0:cutting_point] = pop[r1, 0:cutting_point]
        offspring[2 * i, cutting_point:] = pop[r2, cutting_point:]
        offspring[2 * i + 1, 0:cutting_point] = pop[r2, 0:cutting_point]
        offspring[2 * i + 1, cutting_point:] = pop[r1, cutting_point:]

    return offspring


def mutation(pop, mutation_rate):
    offspring = np.zeros((mutation_rate, pop.shape[1]))
    for i in range(int(mutation_rate / 2)):
        r1 = random.randint(0, pop.shape[0] - 1)
        r2 = random.randint(0, pop.shape[0] - 1)
        while r1 == r2:
            r1 = random.randint(0, pop.shape[0] - 1)
            r2 = random.randint(0, pop.shape[0] - 1)

        cutting_point = random.randint(0, pop.shape[1] - 1)
        offspring[2 * i] = pop[r1]
        offspring[2 * i, cutting_point] = pop[r2, cutting_point]
        offspring[2 * i + 1] = pop[r2]
        offspring[2 * i + 1, cutting_point] = pop[r1, cutting_point]

    return offspring


def local_search(pop, fitness, lower_bounds, upper_bounds, step_size, rate):
    index = np.argmin(fitness)
    offspring = np.zeros((rate * 2 * pop.shape[1], pop.shape[1]))
    for r in range(rate):
        offspring1 = np.zeros((pop.shape[1], pop.shape[1]))
        for i in range(int(pop.shape[1])):
            offspring1[i] = pop[index]
            offspring1[i, i] += np.random.uniform(0, step_size)
            if offspring1[i, i] >= upper_bounds[i]:
                offspring1[i, i] = upper_bounds[i]

        offspring2 = np.zeros((pop.shape[1], pop.shape[1]))
        for i in range(int(pop.shape[1])):
            offspring2[i] = pop[index]
            offspring2[i, i] += np.random.uniform(-step_size, 0)
            if offspring2[i, i] <= lower_bounds[i]:
                offspring2[i, i] = lower_bounds[i]

        offspring12 = np.zeros((2 * pop.shape[1], pop.shape[1]))
        offspring12[0:pop.shape[1]] = offspring1
        offspring12[pop.shape[1]:2 * pop.shape[1]] = offspring2
        offspring[r * 2 * pop.shape[1]:r * 2 * pop.shape[1] + 2 * pop.shape[1]] = offspring12

    return offspring
