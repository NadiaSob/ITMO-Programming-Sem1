import pygame
import random
from pygame.locals import *
from typing import List, Tuple

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:

    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        self.grid = self.create_grid(True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            # Отрисовка списка клеток
            self.draw_lines()
            self.draw_grid()

            # Выполнение одного шага игры (обновление состояния ячеек)
            self.grid = self.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        if randomize:
            return [[random.randint(0, 1) for _ in range(self.cell_width)] for _ in range(self.cell_height)]
        else:
            return [[0 for _ in range(self.cell_width)] for _ in range(self.cell_height)]

    def draw_grid(self) -> None:
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if self.grid[i][j]:
                    color = pygame.Color("green")
                else:
                    color = pygame.Color("white")
                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        j * self.cell_size + 1,
                        i * self.cell_size + 1,
                        self.cell_size - 1,
                        self.cell_size - 1,
                    ),
                )

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbors = []
        row, col = cell
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (
                        (i, j) != (0, 0) and
                        0 <= row + i < self.cell_height and
                        0 <= col + j < self.cell_width
                ):
                    neighbors.append(self.grid[row + i][col + j])
        return neighbors

    def get_next_generation(self) -> Grid:
        next_gen = self.create_grid(False)
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                new_neighbours = self.get_neighbours((i, j)).count(1)
                if (self.grid[i][j] == 0 and new_neighbours == 3) or \
                        (self.grid[i][j] == 1 and new_neighbours in [2, 3]):
                    next_gen[i][j] = 1
        return next_gen


if __name__ == "__main__":
    GameOfLife(400, 400, 20).run()
