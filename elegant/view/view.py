import pygame

class View:
    def __init__(self):
        pygame.init()
        self.view = "start_screen"
        size = width, height = 640, 480
        self.screen = pygame.display.set_mode(size)

        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def draw(self, player):
        if self.view == "start_screen":
            self.screen.fill((124, 124, 124))

            pygame.draw.rect(
                self.screen,
                (255, 0, 0),
                pygame.Rect(50, 50, 50, 50)
            )
            pygame.draw.rect(
                self.screen,
                (0, 255, 0),
                pygame.Rect(150, 50, 50, 50)
            )
            
            pygame.draw.rect(
                self.screen,
                (0, 0, 255),
                pygame.Rect(250, 50, 50, 50)
            )

            if player.color:
                message = f'You clicked {player.color}'
                textsurface = self.font.render(message, False, (255, 255, 255))
                self.screen.blit(textsurface,(50,200))
            
            pygame.display.flip()
