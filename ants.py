import pygame
import colorreader
import numpy as np
from locals import *
from pygame import gfxdraw

pygame.init() # инициализация модулей pygame
global DRAW_LINES, DEFAULT_COLOR, GRID_COLOR, CURRENT_COLOR, TEXT_COLOR, SEQUENCES, SIZE, STEPS_PER_FRAME, LOCALISATION

DRAW_LINES = True # рисовать ли сетку
DEFAULT_COLOR = colorreader.COLORS['def'] # цвет мёртвой клетки
GRID_COLOR    = (80, 80, 80) # цвет сетки
CURRENT_COLOR = (200, 200, 200, 150) # цвет текущей клетки
TEXT_COLOR    = (255, 255, 255) # цвет текста
SEQUENCES = colorreader.receive_sequences()
CELLSIZE  = 10 # размер в пикселях одной клетки
FIELDSIZE = 75 # размер поля в клетках
STEPS_PER_FRAME = 3 # шагов за кадр
LOCALISATION = ENG # RU, ENG, JP, UKR

class GameField:
    def __init__(self, size_of_grid: int, size_of_cell: int, spf: int):
        self.gridsize = size_of_grid
        self.cellsize = size_of_cell

        self.grid = np.array([[Gridcell() for _ in range(size_of_grid)] for _ in range(size_of_grid)]) # 2д массив из клеток
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                self.grid[x, y].x = x
                self.grid[x, y].y = y

        self.display = pygame.display.set_mode((size_of_grid * size_of_cell, size_of_grid * size_of_cell)) # дисплей размером с длину массива умноженную на размер одной клетки
        self.clock = pygame.time.Clock()
        self.spf = spf
        self.steps = 0
        self._current_cell = self.grid[size_of_grid // 2, size_of_grid // 2]
        self._current_dir = 'up'
        pygame.display.set_caption('ANTS') # название окна
    
    def _update_cells(self, iters = 1):
        for seq in range(len(SEQUENCES)):
            if (self._current_cell.color == SEQUENCES[seq]['color']):
                _dir = SEQUENCES[seq]['dir']
                try:
                    oldcell = self._current_cell

                    if (_dir == 'left'):
                        if (self._current_dir == 'up'):
                            self._current_dir = 'left'
                        elif (self._current_dir == 'down'):
                            self._current_dir = 'right'
                        elif (self._current_dir == 'left'):
                            self._current_dir = 'down'
                        elif (self._current_dir == 'right'):
                            self._current_dir = 'up'
                    elif (_dir == 'right'):
                        if (self._current_dir == 'up'):
                            self._current_dir = 'right'
                        elif (self._current_dir == 'down'):
                            self._current_dir = 'left'
                        elif (self._current_dir == 'left'):
                            self._current_dir = 'up'
                        elif (self._current_dir == 'right'):
                            self._current_dir = 'down'

                    if (self._current_dir == 'up'):
                        self._current_cell = self.grid[self._current_cell.x, self._current_cell.y - 1]
                    elif (self._current_dir == 'down'):
                        self._current_cell = self.grid[self._current_cell.x, self._current_cell.y + 1]
                    elif (self._current_dir == 'left'):
                        self._current_cell = self.grid[self._current_cell.x - 1, self._current_cell.y]
                    elif (self._current_dir == 'right'):
                        self._current_cell = self.grid[self._current_cell.x + 1, self._current_cell.y]
                except IndexError:
                    pass
                
                try:
                    oldcell.fill(SEQUENCES[seq + 1]['color']) # закрашивание клетки
                except IndexError:
                    oldcell.fill(SEQUENCES[0]['color'])
                
                break
        self.steps += 1
        if (iters <= 1):
            return
        else:
            return self._update_cells(iters - 1)

    def _draw_cells(self):
        for y in range(len(self.grid)): # зарисовка всех клеток матрицы
            for x in range(len(self.grid[y])):
                # зарисовка одной клетки её цветом
                if (self.grid[x, y] == self._current_cell):
                    gfxdraw.box(self.display, (x * self.cellsize, y * self.cellsize, self.cellsize, self.cellsize), CURRENT_COLOR)
                else:
                    gfxdraw.box(self.display, (x * self.cellsize, y * self.cellsize, self.cellsize, self.cellsize), self.grid[x, y].color)
    
    def _draw_text(self):
        fontsize = (self.gridsize * self.cellsize) // 20
        if (LOCALISATION != JP):
            font = pygame.font.Font('Thintel.ttf', fontsize)
        else:
            font = pygame.font.Font('ChiaroStd-B.otf', int(fontsize // 1.5))
        steps = font.render(f'{LOCALISATION}{self.steps}', 0, TEXT_COLOR)
        self.display.blit(steps, (self.gridsize, fontsize * 2))

    def _draw_gridlines(self): # отрисовка сетки
        for index in range(1, len(self.grid)):
            gfxdraw.line(self.display, 0, index * self.cellsize, self.gridsize * self.cellsize, index * self.cellsize, GRID_COLOR)
        for index in range(1, len(self.grid[0])):
            gfxdraw.line(self.display, index * self.cellsize, 0, index * self.cellsize, self.gridsize * self.cellsize, GRID_COLOR)

    def draw(self): # цикл отрисовки клеток
        self.clock.tick(60)
        self._update_cells(self.spf)
        self._draw_cells()
        if (DRAW_LINES):
            self._draw_gridlines()
        self._draw_text()
        

class Gridcell: 
    def __init__(self):
        self.color = DEFAULT_COLOR

    def fill(self, color): # изменяет цвет клетки
        self.color = color


game = GameField(FIELDSIZE, CELLSIZE, STEPS_PER_FRAME)
while True:
    for e in pygame.event.get(): # слежение за тем, что пользователь нажмёт крестик
        if (e.type == pygame.QUIT):
            quit()

    game.draw()

    pygame.display.update()