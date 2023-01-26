import math

import numpy as np
import pygad

from maze_functions.HandGeneration import maze, cell

lab_size = 10
gene_space = [1, 2, 3, 4]  # up, right, down, left
thirdD_space = [1, 2, 3, 4, 5, 6]  # up, down, left, right, forward, back

space = np.empty((lab_size, lab_size, lab_size), dtype=cell)
labirynth3d = maze(lab_size, space)

labirynth = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, -1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
             [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
             [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0], [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
             [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
             [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 10, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# labir3d = [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
#                # ---
#                [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#                 [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#                 [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
#                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
#                 [0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
#                # ---
#                [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
#                # ---
#                [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
#                 [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
#                 [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
#                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
#                 [0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
#                [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]


def distance_from_exit(solution):
    output = 0.0
    location = [1, 1, 1]
    exit_distance = math.sqrt(100 - location[0] * location[0] + 100 - location[1] * location[1])
    for iterator in range(0, len(solution)):
        if solution[iterator] == 1:
            if labirynth[location[0] - 1][location[1]] > 0:
                location[0] = location[0] - 1
                output = output + (labirynth[location[0]][location[1]] - 0.5)
        elif solution[iterator] == 2:
            if labirynth[location[0]][location[1] + 1] > 0:
                location[1] = location[1] + 1
                output = output + (labirynth[location[0]][location[1]] - 0.5) + 1
        elif solution[iterator] == 3:
            if labirynth[location[0] + 1][location[1]] > 0:
                location[0] = location[0] + 1
                output = output + (labirynth[location[0]][location[1]] - 0.5) + 1
        elif solution[iterator] == 4:
            if labirynth[location[0]][location[1] - 1] > 0:
                location[1] = location[1] - 1
                output = output + (labirynth[location[0]][location[1]] - 0.5)
    return output
    # =-=-=-=-=-=-=-=3D element=-=-=-=-=-=-=#


def get_distance_to_exit(location, size):
    # size = lab_size
    distance = math.sqrt(
        size * size - location[0] * location[0] + size * size - location[1] * location[1] + size * size - location[
            2] * location)


def distance_3d(solution):
    location = [0, 0, 0]
    output = 0.0
    for iterator in range(0, len(solution)):
        temp = [location[0], location[1], location[2]]
        if solution[iterator] == 1:
            if labirynth3d[[location[0]][location[1]][location[2]]].up == 1:
                location[2] = location[2] - 1
                output = output + get_distance_to_exit(location, lab_size) - get_distance_to_exit(temp, lab_size)
        elif solution[iterator] == 2:
            if labirynth3d[[location[0]][location[1]][location[2]]].down == 1:
                location[2] = location[2] + 1
                output = output + get_distance_to_exit(location, lab_size) - get_distance_to_exit(temp, lab_size)
        elif solution[iterator] == 3:
            if labirynth3d[[location[0]][location[1]][location[2]]].left == 1:
                location[1] = location[1] + 1
                output = output + get_distance_to_exit(location, lab_size) - get_distance_to_exit(temp, lab_size)
        elif solution[iterator] == 4:
            if labirynth3d[[location[0]][location[1]][location[2]]].right == 1:
                location[1] = location[1] - 1
                output = output + get_distance_to_exit(location, lab_size) - get_distance_to_exit(temp, lab_size)
        elif solution[iterator] == 5:
            if labirynth3d[[location[0]][location[1]][location[2]]].forward == 1:
                location[0] = location[0] + 1
                output = output + get_distance_to_exit(location, lab_size) - get_distance_to_exit(temp, lab_size)
        elif solution[iterator] == 6:
            if labirynth3d[[location[0]][location[1]][location[2] - 1]].back == 1:
                location[0] = location[0] - 1
                output = output + get_distance_to_exit(location, lab_size) - get_distance_to_exit(temp, lab_size)
    return output


def pathclearer(solution):
    output = 0.0
    location = [1, 1]
    for i in range(0, len(solution)):
        if solution[i] == 1:
            output = output + (-0.5 + labirynth[location[0] - 1][location[1]])
        elif solution[i] == 2:
            output = output + (-0.5 + labirynth[location[0]][location[1] + 1])
        elif solution[i] == 3:
            output = output + (-0.5 + labirynth[location[0] + 1][location[1]])
        elif solution[i] == 4:
            output = output + (-0.5 + labirynth[location[0]][location[1] - 1])
    return output


def fitness_func(solution, solution_idx):
    fitness = distance_from_exit(solution)
    # fitness = pathclearer(solution)
    return fitness


def fitness_3d(solution, solution_idx):
    fitness = distance_3d(solution)
    return fitness


if __name__ == '__main__':
    # fitness_function = fitness_func
    fitness_function = fitness_3d
    sol_per_pop = 30
    num_genes = 45
    num_parents_mating = 7
    num_generations = 60
    keep_parents = 5
    # sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
    parent_selection_type = "rank"
    crossover_type = "single_point"
    mutation_type = "random"
    mutation_percent_genes = 15

    ga_instance = pygad.GA(gene_space=thirdD_space,
                           num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_function,
                           sol_per_pop=sol_per_pop,
                           num_genes=num_genes,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes)
    # ga_instance = pygad.GA(gene_space=gene_space,
    #                        num_generations=num_generations,
    #                        num_parents_mating=num_parents_mating,
    #                        fitness_func=fitness_function,
    #                        sol_per_pop=sol_per_pop,
    #                        num_genes=num_genes,
    #                        parent_selection_type=parent_selection_type,
    #                        keep_parents=keep_parents,
    #                        crossover_type=crossover_type,
    #                        mutation_type=mutation_type,
    #                        mutation_percent_genes=mutation_percent_genes)

    ga_instance.run()

    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    for i in range(0, lab_size):
        line = ""
        for j in range(0, lab_size):
            if labirynth[i][j] == 0:
                line = line + 'xx'
            elif labirynth[i][j] == 1:
                line = line + '  '
            elif labirynth[i][j] == -1:
                line = line + 'ST'
            elif labirynth[i][j] == 10:
                line = line + 'EN'
        print(line)

    print("Parameters of the best solution : {solution}".format(solution=solution))
    print("Fitness value of the best solution ={solution_fitness}".format(solution_fitness=solution_fitness))

    ga_instance.plot_fitness()
