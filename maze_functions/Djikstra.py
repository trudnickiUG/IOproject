import numpy as np


def djikstra_solver(maze, size, start, goal):
    path_grid = np.zeros((size, size, size))

    # step 1 - find shortest path from start to any other point
    path_grid[[start[0], start[1], start[2]]] = 1
    # while [path_grid[0], path_grid[1], path_grid[2]] != [goal[0], goal[1], goal[2]]:
    for i in range(0, size):
        for j in range(0, size):
            for k in range(0, size):
                if maze[i, j, k].up == 1:
                    if path_grid[i, j, k - 1] > path_grid[i, j, k] + 1:
                        path_grid[i, j, k - 1] = path_grid[i, j, k] + 1
                    else:
                        path_grid[i, j, k] = path_grid[i, j, k - 1] + 1
                if maze[i, j, k].down == 1:
                    if path_grid[i, j, k + 1] > path_grid[i, j, k] + 1:
                        path_grid[i, j, k + 1] = path_grid[i, j, k] + 1
                    else:
                        path_grid[i, j, k] = path_grid[i, j, k + 1] + 1
                if maze[i, j, k].left == 1:
                    if path_grid[i - 1, j, k] > path_grid[i, j, k] + 1:
                        path_grid[i - 1, j, k] = path_grid[i, j, k] + 1
                    else:
                        path_grid[i, j, k] = path_grid[i - 1, j, k] + 1
                if maze[i, j, k].right == 1:
                    if path_grid[i + 1, j, k] > path_grid[i, j, k] + 1:
                        path_grid[i + 1, j, k] = path_grid[i, j, k] + 1
                    else:
                        path_grid[i, j, k] = path_grid[i + 1, j, k] + 1
                if maze[i, j, k].forward == 1:
                    if path_grid[i, j + 1, k] > path_grid[i, j, k] + 1:
                        path_grid[i, j + 1, k] = path_grid[i, j, k] + 1
                    else:
                        path_grid[i, j, k] = path_grid[i, j + 1, k] + 1
                if maze[i, j, k].back == 1:
                    if path_grid[i, j - 1, k] > path_grid[i, j, k] + 1:
                        path_grid[i, j - 1, k] = path_grid[i, j, k] + 1
                    else:
                        path_grid[i, j, k] = path_grid[i, j - 1, k] + 1
    #return shortest distance from start to finish
    return path_grid[goal[0], goal[1], goal[2]]
