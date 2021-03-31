import pygame
import math
import random


class Qix:
    # Initialize Qix
    def __init__(self, color) -> None:
        # Qix color
        self.color = color

        # Qix size
        self.radius = 5

        # Qix start position
        self.start_x = 400
        self.start_y = 300

        # Qix end position
        self.end_x = 0
        self.end_y = 0

        # Qix size
        self.length = 0
        self.thickness = 20

        # Qix rotation
        self.rotation = 0

        # Fastest speed at which Qix can travel
        self.max_movement_speed = 10

    # Draw Qix on screen
    def draw(self, surface) -> None:
        self.move()

        # Calculate end point of Qix
        self.end_x = self.start_x + self.length * math.cos(self.rotation)
        self.end_y = self.start_y + self.length * math.sin(self.rotation)

        pygame.draw.circle(surface, self.color,
                           (self.start_x, self.start_y), self.radius)

    # Move Qix Randomly
    def move(self) -> None:
        # Clamp position to be in the playing field
        if self.start_x > 550:
            self.start_x = 550
        elif self.start_x < 250:
            self.start_x = 250
        # add y clamp
        if self.start_y > 450:
            self.start_y = 450
        elif self.start_y < 150:
            self.start_y = 150

        self.start_x += random.uniform(-self.max_movement_speed,
                                       self.max_movement_speed)
        self.start_y += random.uniform(-self.max_movement_speed,
                                       self.max_movement_speed)
