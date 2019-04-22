import sys

import pygame

from elegant.model import Player
from elegant.view import View

class Controller:
    def __init__(self):
        self.player = Player("Player 1")
        self.view = View()
        self.run()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                self.player.set_color(x, y)

        
    def run(self):
        while True:
            self.process_events()
            self.view.draw(self.player)
