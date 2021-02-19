import curses
from time import sleep
from life import GameOfLife
from ui import UI


class Console(UI):

    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)
        self.screen = curses.initscr()

    def draw_borders(self) -> None:
        self.screen.border(0)

    def draw_grid(self) -> None:
        for i in range(1, len(self.life.curr_generation) - 1):
            for j in range(1, len(self.life.curr_generation[i]) - 1):
                if self.life.curr_generation[i][j]:
                    sign = "*"
                else:
                    sign = " "
                self.screen.addch(i, j, sign)

    def run(self) -> None:
        self.draw_borders()
        running = True
        while running:
            self.draw_borders()
            self.draw_grid()
            self.screen.refresh()
            sleep(0.3)
            self.life.step()
        curses.endwin()


if __name__ == "__main__":
    life = GameOfLife((30, 30))
    Console(life).run()
