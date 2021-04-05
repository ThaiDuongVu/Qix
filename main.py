import sys
import math
import pygame
from pygame.locals import *

from point import Point
from grid import Grid
from player import Player
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
red = (236, 70, 70)
orange = (255, 176, 55)
blue = (0, 173, 181)

text_font = pygame.font.Font("font.ttf", 36)

# Current game score
score = 0
# Game clock
clock = pygame.time.Clock()


# Quit current game
def quit_game() -> None:
    pygame.quit()
    sys.exit()


# Main game loop
def main_loop() -> None:
    game_exit = False
    game_over = False
    game_won = False

    grid = Grid(50, 50, blue, black, white, white)
    player = Player(red)
    sparx1 = Sparx(orange, "right")
    sparx2 = Sparx(orange, "left")
    qix = Qix(orange)

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
                    player.velocity_x = 0
                    player.velocity_y = -1
                if event.key == K_DOWN:
                    player.velocity_x = 0
                    player.velocity_y = 1
                if event.key == K_LEFT:
                    player.velocity_x = -1
                    player.velocity_y = 0
                if event.key == K_RIGHT:
                    player.velocity_x = 1
                    player.velocity_y = 0

                # If space button pressed then enable player pushing
                if event.key == K_SPACE:
                    player.is_pusing = True

                # If enter button pressed then restart game
                if event.key == K_RETURN:
                    if game_over:
                        main_loop()

            if event.type == KEYUP:
                # If arrow keys released then stop moving player
                if event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT:
                    player.velocity_x = player.velocity_y = 0

                # If space button released then disable player pushing
                if event.key == K_SPACE:
                    player.is_pusing = False

        # Check collision between player and sparxs
        if player.x == sparx1.x and player.y == sparx2.y:
            player.health -= 1
        if player.x == sparx2.x and player.y == sparx2.y:
            player.health -= 1

        # If player run out of health then game over
        if player.health <= 0:
            game_over = True

        # If the claimed percentage is higher than 75% then player wins
        if int(grid.claimed_percent) > 75:
            game_over = True
            game_won = True

        # Render game objects
        if not game_over:
            game_surface.fill(black)
            grid.draw(game_surface)
            player.draw(game_surface, grid)
            sparx1.draw(game_surface, grid)
            sparx2.draw(game_surface, grid)
            qix.draw(game_surface)

            game_surface.blit(text_font.render(
                "Claimed    " + str(int(grid.claimed_percent)), True, white), [520, 20])
            game_surface.blit(text_font.render(
                "Health        " + str(player.health), True, white), [520, 60])
        else:
            game_surface.fill(black)
            if game_won:
                game_surface.blit(text_font.render(
                    "You    Won!", True, white), [300, 100])
            else:
                game_surface.blit(text_font.render(
                    "Game    Over", True, white), [300, 100])
            game_surface.blit(text_font.render(
                "Press    Enter    to    restart    game", True, white), [140, 200])

        # Render game at 60 frames per second
        clock.tick(60)

        # Update render display
        pygame.display.update()

    quit_game()


if __name__ == "__main__":
    main_loop()
