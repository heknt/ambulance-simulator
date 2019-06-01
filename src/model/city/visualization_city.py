from abc import ABC, abstractmethod
import pygame
from src.model.singleton import Singleton
from src.model.city.city import *

WINDOW_TITLE = "Ambulance Car On The City"
WIDTH = 800
HEIGHT = 608
FPS = 40


class Drawer(ABC):
    def draw(self):
        pass


class Handler(ABC):
    def handle_events(self):
        pass


class Updater(ABC):
    def update(self):
        pass


class Game(Drawer, Handler, Updater):
    done = False
    color_bg = pygame.Color('darkgrey')

    @abstractmethod
    def main_loop(self):
        pass


class VisualCity(Game, Singleton):
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)

        self.clock = pygame.time.Clock()
        self.limit_fps = True
        self.now = 0

    def main_loop(self):
        while not self.done:
            self.handle_events()
            self.update()
            self.draw()

            if self.limit_fps:
                self.clock.tick(FPS)
            else:
                self.clock.tick()

    def draw(self):
        self.screen.fill(self.color_bg)
        Map(self.screen)

        pygame.display.flip()

    def update(self):
        self.now = pygame.time.get_ticks()

    def handle_events(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.done = True


if __name__ == "__main__":
    visual_city = VisualCity()
    visual_city.main_loop()
