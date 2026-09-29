"""Класс сетки."""

import pygame

from settings import (
    CELL_SIZE, COLOR_GRID, COLOR_CELL,
    COLOR_WALL, COLOR_START, COLOR_FINISH,
)

EMPTY = 0
WALL = 1
START = 2
FINISH = 3


class Grid:

    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.cells = [[EMPTY for _ in range(cols)] for _ in range(rows)]
        self.start = (0, 0)
        self.finish = (cols - 1, rows - 1)
        self.cells[0][0] = START
        self.cells[rows - 1][cols - 1] = FINISH

    def draw(self, surface):
        for row in range(self.rows):
            for col in range(self.cols):
                rect = pygame.Rect(
                    col * CELL_SIZE,
                    row * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE,
                )
                cell_type = self.cells[row][col]
                color = self._color_for(cell_type)
                pygame.draw.rect(surface, color, rect)
                pygame.draw.rect(surface, COLOR_GRID, rect, 1)

    def _color_for(self, cell_type):
        if cell_type == WALL:
            return COLOR_WALL
        if cell_type == START:
            return COLOR_START
        if cell_type == FINISH:
            return COLOR_FINISH
        return COLOR_CELL

    def set_cell(self, col, row, cell_type):
        self.cells[row][col] = cell_type

    def clear(self):
        self.cells = [[EMPTY for _ in range(self.cols)]
                      for _ in range(self.rows)]