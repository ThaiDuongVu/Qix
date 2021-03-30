import sys
import math
import pygame
from pygame.locals import *

from player import Player
from border import Border
from sparx import Sparx
from qix import Qix

# Initialize pygame library
pygame.init()

# Set screen width & height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
game_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set screen caption
CAPTION = "Qix"
pygame.display.set_caption(CAPTION)

# Set game icon
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Initialize global variables here
black = (34, 40, 49)
white = (238, 238, 238)
blue = (0, 173, 181)
red = (236, 70, 70)

text_font = pygame.font.Font("font.ttf", 36)

# Current game score
score = 0

clock = pygame.time.Clock()


# Quit current game
def quit_game() -> None:
    pygame.quit()
    sys.exit()

def check_player_Qix_collision(player,qix) -> bool:
     d= math.sqrt( (player.x - qix.start_x)** 2 + (player.y - qix.start_y)**2 )
     if (d <=  qix.radius ):
         return True
     return False

def check_player_Sparx_Collision(player,sparx1,sparx2) -> bool:
    d1= math.sqrt( (player.x - sparx1.x)** 2 + (player.y - sparx1.y)**2 )
    d2=  math.sqrt( (player.x - sparx2.x)** 2 + (player.y - sparx2.y)**2 )
    if (d1 <=  sparx1.radius) or (d2 <=  sparx1.radius):
         return True
    return False

# Main game loop
def main_loop() -> None:
    game_exit = False
    game_over = False

    border = Border(white)

    player = Player(blue, border)
    sparx1 = Sparx(red, "right", border)
    sparx2 = Sparx(red, "left", border)

    qix = Qix(red)

    while not game_exit:
        for event in pygame.event.get():
            # Exit game if window closed
            if event.type == QUIT:
                game_exit = True
 
        
            if event.type == KEYDOWN:
                # Quit game when escape key is pressed
                if event.key == K_ESCAPE:
                    game_exit = True

                # Move player with arrow keys
                if event.key == K_UP:
                    player.start_moving(0, -1)
                if event.key == K_DOWN:
                    player.start_moving(0, 1)
                if event.key == K_LEFT:
                    player.start_moving(-1, 0)
                if event.key == K_RIGHT:
                    player.start_moving(1, 0)

                # If space button down then enable player pushing
                if event.key == K_SPACE:
                    if game_over:
                        main_loop()
                    else:
                        player.is_pushing = True

            if event.type == KEYUP:
                # Stop moving player on arrow keys released
                if event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT:
                    player.stop_moving()

                # If space button released then disable player pushing
                if event.key == K_SPACE:
                    player.is_pushing = False
        
        #If Qix collides with player, reset position + health decreases
        if (check_player_Qix_collision(player,qix)):
            qix.__init__(red)
            player.decreaseHealth()
            player.resetPosition()
            
        #If Sparc collides with player, reset position + health decreases
        if (check_player_Sparx_Collision(player, sparx1, sparx2)):
            sparx1.__init__(red, "right", border)
            sparx2.__init__(red, "left", border)
            player.decreaseHealth()
            player.resetPosition()
            
        # Fill black background
        game_surface.fill(black)

        # Render game objects
        if not game_over:
            border.draw(game_surface)
            player.draw(game_surface)
            sparx1.draw(game_surface, border)
            sparx2.draw(game_surface, border)
            qix.draw(game_surface)
        else:
            game_surface.blit(text_font.render(
                "Game    Over", True, white), [300, 100])
            game_surface.blit(text_font.render(
                "Press    Space    to    restart    game", True, white), [140, 200])

        # Render game at 60 frames per second
        clock.tick(60)

        # Update render display
        pygame.display.update()

    quit_game()


if __name__ == "__main__":
    main_loop()
