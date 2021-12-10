"""
    This algorithm uses 2 matris to visualise a magic cube.
    Matrices are being changed based on perspective.
    The point of perspective is one side of cube.

    Cubist.move function moves the given matrices.
    If you want to move cube's 1st row to left direction,parameter is '1hL'
    1hL = 1st Horizontal line to Left
    When you moved cube that way(1hL) also cube's upside matris changes clockwise.
    Because as I said before it is based on perspective.

    Cubist.move :param examples:
        2vU = 2nd Vertical line to Up
        3vD = 3th Vertical line to Down
        1hR = 1st Horizontal line to Right
        ...

    Visualization is made via using pygame.Block class uses cube's matrices to visualise magic cube.

    ToDo:
        Whenever I learn solving magic cubes, solving algorithms will be added.
"""
import pygame
from random import randint, choice
import copy

pygame.init()
cube_horizontal = [[[i, i, i] for i in ['green', 'orange', 'blue', 'red']] for t in range(3)]
cube_vertical = [[[i, i, i] for i in ['yellow', 'green', 'white']] for _ in range(3)]
cube = {'h': cube_horizontal, 'v': cube_vertical}

class Cubist:
    def __init__(self, cube_dict):
        self.cube_dict = cube_dict
        self.__n = len(self.cube_dict['v'])

    def move(self, movement):
        index, vector, direction = movement
        index = int(index) - 1
        if vector == 'h':
            shifted_side_lines = [None for i in range(4)]
            if direction == 'R':
                for i, side_line in enumerate(self.cube_dict['h'][index]):
                    if i == 3:
                        shifted_side_lines[0] = side_line
                        continue
                    shifted_side_lines[i + 1] = side_line
                if index == self.__n - 1:
                    self.clockwise(self.cube_dict['v'], index, self.__n, vector, reverse=True)
                if index == 0:
                    #Need to fix reverse algorithm for this condition
                    self.clockwise(self.cube_dict['v'], index, self.__n, vector)
                    self.clockwise(self.cube_dict['v'], index, self.__n, vector)
                    self.clockwise(self.cube_dict['v'], index, self.__n, vector)


            elif direction == 'L':
                for i, side_line in enumerate(self.cube_dict['h'][index]):
                    if i == 0:
                        shifted_side_lines[3] = side_line
                        continue
                    shifted_side_lines[i - 1] = side_line
                if index == 0 or index == self.__n - 1:
                    self.clockwise(self.cube_dict['v'], index, self.__n, vector)

            self.cube_dict['h'][index] = shifted_side_lines
            self.cube_dict['v'][index][1] = shifted_side_lines[0]

        elif vector == 'v':
            temp_dict = copy.deepcopy(self.cube_dict)
            if direction == 'U':
                for side_index, (h_line, v_line) in enumerate(zip(temp_dict['h'], temp_dict['v'])):
                    self.cube_dict['v'][side_index][0][index] = h_line[0][index]
                    self.cube_dict['h'][side_index][0][index] = v_line[2][index]
                    self.cube_dict['v'][abs(side_index - 2)][2][index] = list(reversed(h_line[2]))[index]
                    self.cube_dict['h'][abs(side_index - 2)][2][self.__n - index - 1] = v_line[0][index]
                if index == 0:
                    self.clockwise(self.cube_dict['h'], 3, 3, vector, reverse=True)
                if index == self.__n - 1:
                    self.clockwise(self.cube_dict['h'], 1, 3, vector)

            elif direction == 'D':
                for side_index, (h_line, v_line) in enumerate(zip(temp_dict['h'], temp_dict['v'])):
                    self.cube_dict['v'][abs(side_index - 2)][0][index] = list(reversed(h_line[2]))[index]
                    self.cube_dict['h'][side_index][0][index] = v_line[0][index]
                    self.cube_dict['v'][side_index][2][index] = h_line[0][index]
                    self.cube_dict['h'][abs(side_index - 2)][2][self.__n - index - 1] = v_line[2][index]
                if index == 0:
                    self.clockwise(self.cube_dict['h'], 3, 3, vector)
                if index == self.__n - 1:
                    self.clockwise(self.cube_dict['h'], 1, 3, vector, reverse=True)
            for i in range(3):
                self.cube_dict['v'][i][1] = self.cube_dict['h'][i][0]

    @staticmethod
    def clockwise(matris, side_index, n, vector, reverse=False):
        side_matris = [[*range(n)] for i in range(n)]
        for i, side_lines in enumerate(matris):
            side_line = side_lines[side_index]
            side_line = list(reversed(side_line))
            for y in range(n):
                side_matris[y][i] = side_line[y]
        for i, side_lines in enumerate(matris):
            if reverse:
                if vector == 'h':
                    matris[abs(i - 2)][side_index] = list(reversed(side_matris[i]))
                elif vector == 'v':
                    matris[i][side_index] = side_matris[i]
                continue
            if vector == 'v':
                matris[abs(i - 2)][side_index] = list(reversed(side_matris[i]))
            elif vector == 'h':
                matris[abs(i - 2)][side_index] = list(reversed(side_matris[i]))

    def random_move(self):
        pos = str(randint(1,3))
        vector = choice(['v', 'h'])
        movement = pos + vector
        if vector == 'v':
            movement += choice(['U', 'D'])
        else:
            movement += choice(['R', 'L'])
        self.move(movement)
        Block.block_maker(self.cube_dict)


class Block(pygame.sprite.Sprite):
    _blocks = pygame.sprite.Group()
    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    def __init__(self, surface, color, x, y, width = 30, height = 30):
        super().__init__()
        self.surface = surface
        self.color = color
        self.image = pygame.Rect(x, y, width, height)
        Block._blocks.add(self)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.image)

    @classmethod
    def main(cls):
        for block in cls._blocks:  #bloklarin canlarini ekrana ekleme
            block.draw()
        cls._blocks = pygame.sprite.Group()

    @staticmethod
    def block_maker(cube_dict):
        for row, side_lines in enumerate(cube_dict['v']):
            for side_index, side_line in enumerate(side_lines):
                for line_index, block_color in enumerate(side_line):
                    Block(Block.window, block_color, 200+line_index*33, 150 + row*33 + side_index*105)

        for row, side_lines in enumerate(cube_dict['h']):
            for side_index, side_line in enumerate(side_lines):
                for line_index, block_color in enumerate(side_line):
                    Block(Block.window, block_color, 200+side_index*106+line_index*33, 159 + row*33+96)

    @classmethod
    def update(cls, cube_dict):
        cls.window.fill((0, 0, 0))
        cls.block_maker(cube_dict)
        Block.main()
        pygame.display.update()

import time
if __name__ == '__main__':
    cuber = Cubist(cube)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        cuber.random_move()
        Block.update(cuber.cube_dict)
        time.sleep(0.5)