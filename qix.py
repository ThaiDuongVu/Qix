import pygame
import random
from player import Player


class Qix:
    # Initialize Qix
    def __init__(self, color) -> None:
        # Qix color
        self.color = color

        # Qix current position
        self.x = 240
        self.y = 240

        # Qix size
        self.width = 120
        self.height = 5

        # Qix current velocity
        self.velocity_x = 0
        self.velocity_y = 0

    # Draw Qix on game surface
    def draw(self, game_surface) -> None:
        pygame.draw.rect(game_surface, self.color, [
                         self.x, self.y, self.width, self.height])

    # Qix move randomly on game screen
    def move(self) -> None:
        self.x += self.velocity_x * 5
        self.y += self.velocity_y * 5

        self.velocity_x = random.uniform(-1, 1)
        self.velocity_y = random.uniform(-1, 1)

    # Check if qix is colliding with player
    def check_collision_player(self, player: Player) -> None:
        if player.x + player.width >= self.x >= player.x - self.width:
            if player.y + player.height >= self.y >= player.y - self.height:
                return True
        return False
