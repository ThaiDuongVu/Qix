import pygame


class Qix:
    # Initialize Qix
    def __init__(self, color) -> None:
        # Qix color
        self.color = color

        # Qix size
        self.radius = 5

        # Qix current position
        self.x = 240
        self.y = 240

        # Qix size
        self.width = 10
        self.height = 10

        # Qix current velocity
        self.velocity_x = 0
        self.velocity_y = 0

    # Draw Qix on game surface
    def draw(self, game_surface) -> None:
        pygame.draw.rect(game_surface, self.color, [
                         self.x, self.y, self.width, self.height])
