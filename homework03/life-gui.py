import pygame
from pygame.locals import *
from life import GameOfLife
from ui import UI


class GUI(UI):

    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed
        self.height = self.life.rows * self.cell_size
        self.width = self.life.cols * self.cell_size
        self.screen_size = self.width, self.height
        self.screen = pygame.display.set_mode(self.screen_size)

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def draw_grid(self) -> None:
        for i in range(self.life.rows):
            for j in range(self.life.cols):
                if self.life.curr_generation[i][j]:
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

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        running = True
        paused = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    (y, x) = pygame.mouse.get_pos()
                    cell_x = x // self.cell_size
                    cell_y = y // self.cell_size
                    if self.life.curr_generation[cell_x][cell_y]:
                        self.life.curr_generation[cell_x][cell_y] = 0
                    else:
                        self.life.curr_generation[cell_x][cell_y] = 1

                    self.draw_lines()
                    self.draw_grid()
                    pygame.display.flip()
                    clock.tick(self.speed)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = not paused

            if not paused:
                self.life.step()
            self.draw_lines()
            self.draw_grid()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


def main():
    game = GameOfLife(size=(30, 30))
    GUI(game).run()


if __name__ == '__main__':
    main()
