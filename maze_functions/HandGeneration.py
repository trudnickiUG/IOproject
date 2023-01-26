import random

import numpy as np

maze_dim = 5


class cell:
    def __init__(self):
        self.up = 0  # directions take 0 for wall and 1 for passage
        self.down = 0
        self.left = 0
        self.right = 0
        self.forward = 0
        self.back = 0
        self.entrance = 0  # 0 default, 1-6 in order directions
        self.visited = 'u'  # u unvisited, v visited, a added

    def update_visit(self, visit):
        self.visited = visit


class maze:

    def __init__(self, side_length, newspace):
        self.space = newspace
        direction = 0
        startpoints_list = []
        for i in range(0, side_length):
            for j in range(0, side_length):
                for k in range(side_length):
                    self.space[i, j, k] = cell()
                    startpoints_list.append([i, j, k])
                    # for k in range(0, side_length + 2):

        random_starter = [4, 0, 3]
        startpoints_list.remove([random_starter[0], random_starter[1], random_starter[2]])
        while len(startpoints_list) > 0:

            start_loc = [random.randrange(0, side_length), random.randrange(0, side_length),
                         random.randrange(0, side_length)]
            walk_loc = [start_loc[0], start_loc[1], start_loc[2]]

            while walk_loc in startpoints_list:
                direction = random.randrange(1, 7)
                self.space[walk_loc[0], walk_loc[1], walk_loc[2]].visited = 'v'
                if direction == 1 and walk_loc[2] - 1 >= 0:  # x is left-right, y is forward-backward, z is up-down
                    # labirynth generated from the top layer, top-left corner
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].up = 1
                    walk_loc[2] = walk_loc[2] - 1
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].down = 1
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].entrance = direction
                elif direction == 2 and walk_loc[2] + 1 < maze_dim:
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].down = 1
                    walk_loc[2] = walk_loc[2] + 1
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].up = 1
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].entrance = direction
                elif direction == 3 and walk_loc[0] - 1 >= 0:
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].left = 1
                    walk_loc[0] = walk_loc[0] - 1
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].entrance = direction
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].right = 1
                elif direction == 4 and walk_loc[0] + 1 < maze_dim:
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].right = 1
                    walk_loc[0] = walk_loc[0] + 1
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].entrance = direction
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].left = 1
                elif direction == 5 and walk_loc[1] - 1 >= 0:
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].forward = 1
                    walk_loc[1] = walk_loc[1] - 1
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].entrance = direction
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].back = 1
                elif direction == 6 and walk_loc[1] + 1 < maze_dim:
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].back = 1
                    walk_loc[1] = walk_loc[1] + 1
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].entrance = direction
                    self.space[walk_loc[0], walk_loc[1], walk_loc[2]].forward = 1

            while [start_loc[0], start_loc[1],          #going from current randwalk start to add cells to labirynth
                   start_loc[2]] in startpoints_list:  # up, down, left, right, forward, back for 1-6
                if [start_loc[0], start_loc[1], start_loc[2]] in startpoints_list:
                    startpoints_list.remove([start_loc[0], start_loc[1], start_loc[2]])
                if self.space[walk_loc[0], walk_loc[1], walk_loc[2]].entrance == 1:
                    start_loc[2] = start_loc[2] - 1
                elif self.space[walk_loc[0], walk_loc[1], walk_loc[2]].entrance == 2:
                    start_loc[2] = start_loc[2] + 1
                elif self.space[walk_loc[0], walk_loc[1], walk_loc[2]].entrance == 3:
                    start_loc[0] = start_loc[0] - 1
                elif self.space[walk_loc[0], walk_loc[1], walk_loc[2]].entrance == 4:
                    start_loc[0] = start_loc[0] + 1
                elif self.space[walk_loc[0], walk_loc[1], walk_loc[2]].entrance == 5:
                    start_loc[0] = start_loc[1] - 1
                elif self.space[walk_loc[0], walk_loc[1], walk_loc[2]].entrance == 6:
                    start_loc[0] = start_loc[1] + 1