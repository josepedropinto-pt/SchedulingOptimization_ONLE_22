#!/usr/bin/python3
import numpy as np
import hybrid
from time import process_time
import matplotlib.pyplot as plt
import pandas as pd
from numpy import mean
pesos = np.arange(0.01, 1, 0.01)
final_costs = []
final_deflex = []
final_fo = []
for p in pesos:
    t1_start = process_time()

    pop_size = 50
    crossover_rate = 110
    mutation_rate = 110
    rate = 10
    no_variables = 4
    lower_bounds = [0.0032, 0.0025, 0.0025, 0.0032]
    upper_bounds = [0.127, 0.254, 0.254, 0.127]

    step_size = (upper_bounds[0] - lower_bounds[0]) * 0.02
    computing_time = 30
    no_generations = 200
    pop = np.zeros((pop_size, no_variables))
    for s in range(pop_size):
        for h in range(no_variables):
            pop[s, h] = np.random.uniform(lower_bounds[h], upper_bounds[h])

    extended_pop = np.zeros((pop_size + crossover_rate + mutation_rate + 2 * no_variables * rate, pop.shape[1]))
    # fig = plt.figure()
    # ax = fig.add_subplot()
    # fig.show()
    # plt.title('Red = min')
    # plt.xlabel("Iterations")
    # plt.ylabel('Objetive Function')

    # A = []
    # B = []
    # a = 5
    # g = 0
    # global_best = pop[0]
    # k = 0

    A = []
    B = []
    a = 5
    g = 0
    global_best = pop[0]
    k = 0
    while g <= no_generations:
        for i in range(no_generations):
            offspring1 = hybrid.crossover(pop, crossover_rate)
            offspring2 = hybrid.mutation(pop, mutation_rate)
            fitness = hybrid.objetctive_function(pop, p)
            offspring3 = hybrid.local_search(pop, fitness, lower_bounds, upper_bounds, step_size, rate)
            step_size = step_size * 0.98
            if step_size < 0.01:
                step_size = 0.01
            extended_pop[0:pop_size] = pop
            extended_pop[pop_size:pop_size + crossover_rate] = offspring1
            extended_pop[pop_size + crossover_rate:pop_size + crossover_rate + mutation_rate] = offspring2
            extended_pop[
            pop_size + crossover_rate + mutation_rate: pop_size + crossover_rate + mutation_rate + 2 * no_variables * rate] = offspring3
            fitness = hybrid.objetctive_function(extended_pop, p)
            pop = hybrid.selection(extended_pop, fitness, pop_size)

            # print(f'Generation: {g} Current best fitness: {min(fitness)}')
            A.append(min(fitness))
            final_fo.append(min(fitness))

            g += 1

            if i >= a:
                if sum(abs(np.diff(A[g - a:g]))) <= 0.0001:
                    index = np.argmin(fitness)
                    current_best = extended_pop[index]
                    pop = np.zeros((pop_size, no_variables))
                    for s in range(pop_size - 1):
                        for h in range(no_variables):
                            pop[s, h] = np.random.uniform(lower_bounds[h], upper_bounds[h])
                    pop[pop_size - 1:pop_size] = current_best
                    step_size = (upper_bounds[0] - lower_bounds[0]) * 0.02
                    global_best = np.vstack((global_best, current_best))
                    break
            # ax.plot(A, color='r')
            # fig.canvas.draw()
            # ax.set_xlim(left=max(0, g - no_generations), right=g + 3)
            t1_stop = process_time()
            time_elapsed = t1_stop - t1_start
            if g > no_generations:
                break
        if g > no_generations:
            break

    fitness = hybrid.objetctive_function(global_best, p)
    index = np.argmin(fitness)
    print("best solution " + str(global_best[index]))
    print("best fitness " + str(min(fitness)))
    print("Real cost " + str(hybrid.cost_fixed(global_best[index])))
    print("Real Deflex " + str(hybrid.deflex_fixed(global_best[index])))
    final_costs.append(hybrid.cost_fixed(global_best[index]))
    final_deflex.append(hybrid.deflex_fixed(global_best[index]))

    # df = pd.DataFrame({
    #     'x_axis': final_costs,
    #     'y_axis': final_deflex})
    # plt.autoscale(enable=True, axis='both', tight=None)
    # plt.plot('x_axis', 'y_axis', data=df, linestyle='-', marker='o', color='r', label='Min dist')
    # plt.pause(0.1)
print('This is deflex array')
print(final_deflex)
print('This is cost array')
print(final_costs)
# print('this is final FO')
# print(final_fo)
# plt.show()

