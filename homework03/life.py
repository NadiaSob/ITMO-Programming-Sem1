import pathlib
import random

from typing import List, Optional, Tuple


Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:

    def __init__(
        self,
        size: Tuple[int, int],
        randomize: bool = True,
        max_generations: Optional[float] = float('inf')
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        if randomize:
            return [[random.randint(0, 1) for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            return [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbors = []
        row, col = cell
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (
                        (i, j) != (0, 0) and
                        0 <= row + i < self.rows and
                        0 <= col + j < self.cols
                ):
                    neighbors.append(self.curr_generation[row + i][col + j])
        return neighbors

    def get_next_generation(self) -> Grid:
        next_gen = self.create_grid(False)
        for i in range(self.rows):
            for j in range(self.cols):
                new_neighbours = self.get_neighbours((i, j)).count(1)
                if (self.curr_generation[i][j] == 0 and new_neighbours == 3) or \
                        (self.curr_generation[i][j] == 1 and new_neighbours in [2, 3]):
                    next_gen[i][j] = 1
        return next_gen

    def step(self) -> None:
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        return self.generations >= self.max_generations

    @property
    def is_changing(self) -> bool:
        return self.curr_generation != self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> 'GameOfLife':
        with open(filename) as file:
            grid = [[int(char) for char in list(line)] for line in file.readline()]
        game = GameOfLife((len(grid), len(grid[0])))
        game.curr_generation = grid
        return game

    def save(self, filename: pathlib.Path) -> None:
        with open(filename) as file:
            for row in self.curr_generation:
                file.write("".join([str(char) for char in row]))
                file.write("\n")