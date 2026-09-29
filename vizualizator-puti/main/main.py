"""Точка входа в приложение."""

import pygame
import sys

from settings import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from grid import Grid


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Визуализатор алгоритмов поиска пути")
    clock = pygame.time.Clock()

    grid = Grid(cols=30, rows=20)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((30, 30, 40))
        grid.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()