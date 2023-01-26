import matplotlib.pyplot as plt
import numpy as np

NORTH = 0
EAST = 1
DOWN = 1

width = 10
height = 10
depth = 10
grid = np.zeros((width, height, depth, 3), bool)


def north(cell):
    return cell[0], cell[1] + 1, cell[2]


def south(cell):
    return cell[0], cell[1] - 1, cell[2]


def east(cell):
    return cell[0] + 1, cell[1], cell[2]


def west(cell):
    return cell[0] - 1, cell[1], cell[2]


def up(cell):
    return cell[0], cell[1], cell[2] + 1

def down(cell):
    return cell[0], cell[1], cell[2] - 1

# can_go_north = grid[i, j][NORTH]
# can_go_east = grid[i, j][EAST]
# can_go_south = grid[south((i, j))][NORTH]
# can_go_west = grid[west((i, j))][EAST]


def draw_maze(grid):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    width = grid.shape[0]
    height = grid.shape[1]

    # draw the south and west outer walls
    plt.plot([0, width], [0, 0], color="black")
    plt.plot([0, 0], [0, height], color="black")

    for j in range(height):
        for i in range(width):
            value = grid[i, j]

            if not value[EAST]:
                # draw a east wall
                plt.plot([i + 1, i + 1], [j, j + 1], color="black")

            if not value[NORTH]:
                # draw a north wall
                plt.plot([i, i + 1], [j + 1, j + 1], color="black")


plt.show()
