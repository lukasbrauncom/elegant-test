from __future__ import division
import pygame
from os import path

## assets folder
img_dir = path.join(path.dirname(__file__), 'Images')
sound_folder = path.join(path.dirname(__file__), 'Sounds')

###############################
## to be placed in "constant.py" later
WIDTH = 1024
HEIGHT = 768
FPS = 60

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
###############################

###############################
## to placed in "__init__.py" later
## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("elegANT: Can you Anticipate What Happens Next?")
clock = pygame.time.Clock()     ## For syncing the FPS
###############################

font_name = pygame.font.match_font('Chaparral Pro')
font2 = pygame.font.SysFont('Chaparral Pro', 80)

def main_menu():
    global screen

    menu_song = pygame.mixer.music.load(path.join(sound_folder, "Ant1hour.mp3"))
    pygame.mixer.music.play(-1)

    title = pygame.image.load(path.join(img_dir, "fireants1024.jpg")).convert()
    title = pygame.transform.scale(title, (WIDTH, HEIGHT), screen)

    screen.blit(title, (0,0))
    pygame.display.update()

    while True:
        ev = pygame.event.poll()
        #?built-in quit for development
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN:
                break
            elif ev.key == pygame.K_q:
                pygame.display.quit()
                pygame.quit()
                quit()
        elif ev.type == pygame.QUIT:
                pygame.quit()
                quit()
        else:
            
            text = font2.render("Press [ENTER] To Begin", True, GREEN, BLACK) 
            textRect = text.get_rect()
            textRect.center = (WIDTH // 2, HEIGHT // 2)
            screen.blit(text, textRect)
            
            
            text2 = font2.render("or [Q] To Quit", True, RED, BLACK) 
            textRect2 = text2.get_rect()
            textRect2.center = (WIDTH // 2, (HEIGHT // 2)+90)
            screen.blit(text2, textRect2)
            
            pygame.display.update()

    #pygame.mixer.music.stop()
    ready = pygame.mixer.Sound(path.join(sound_folder,'battletime.ogg'))
    ready.play()
    screen.fill(BLACK)
    text3 = font2.render("HERE WE GO!", True, WHITE, BLACK)
    textRect3 = text3.get_rect()
    textRect3.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text3, textRect3)
    pygame.display.update()

## Game loop
running = True
menu_display = True
while running:
    if menu_display:
        main_menu()
        pygame.time.wait(30)
        
pygame.quit()
