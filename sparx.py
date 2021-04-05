import pygame
from pygame.locals import *
from grid import Grid
from point import PATH, TRAVERSABLE


class Sparx:
    # Initialize sparx
    def __init__(self, color, init_direction) -> None:
        # Sparx color
        self.color = color

        # Sparx current position
        self.x = 240
        self.y = 0

        # Speed at which sparx will move at
        self.velocity_x = 0
        self.velocity_y = 0

        # Sparx size, should be equal to point size (see point.py)
        self.width = 10
        self.height = 10

        # Initial direction that Sparx will move at, either "right" or "left"
        self.init_direction = init_direction

        if self.init_direction == "right":
            self.velocity_x = 1
        else:
            self.velocity_x = -1

    # Draw sparx on game surface
    def draw(self, game_surface, grid: Grid) -> None:
        self.move(grid)
        pygame.draw.rect(game_surface, self.color, [
                         self.x, self.y, self.width, self.height])

    def change_direction_vertically(self, grid: Grid) -> None:
        if self.y // self.height + 1 < grid.height and (grid.points[self.x // self.width][self.y // self.height + 1].state == TRAVERSABLE or grid.points[self.x // self.width][self.y // self.height + 1].state == PATH):
            self.velocity_x = 0
            self.velocity_y = 1
        if self.y // self.height - 1 >= 0 and (grid.points[self.x // self.width][self.y // self.height - 1].state == TRAVERSABLE or grid.points[self.x // self.width][self.y // self.height - 1].state == PATH):
            self.velocity_x = 0
            self.velocity_y = -1
    
    def change_direction_horizontally(self, grid: Grid) -> None:
        if self.x // self.width + 1 < grid.width and (grid.points[self.x // self.width + 1][self.y // self.height].state == TRAVERSABLE or grid.points[self.x // self.width + 1][self.y // self.height].state == PATH):
            self.velocity_x = 1
            self.velocity_y = 0
        if self.x // self.width - 1 >= 0 and (grid.points[self.x // self.width - 1][self.y // self.height].state == TRAVERSABLE or grid.points[self.x // self.width - 1][self.y // self.height].state == PATH):
            self.velocity_x = -1
            self.velocity_y = 0

    # Move sparx along grid
    def move(self, grid: Grid) -> None:
        # Check next point on grid and change velocity if needed
        # If sparx is moving to the right and next point is not traversable
        if self.velocity_x == 1 and (self.x // self.width + 1 >= grid.width or grid.points[self.x // self.width + 1][self.y // self.height].state != TRAVERSABLE):
            self.change_direction_vertically(grid)
        # If sparx is moving to the left and next point is not traversable
        if self.velocity_x == -1 and (self.x // self.width - 1 < 0 or grid.points[self.x // self.width - 1][self.y // self.height].state != TRAVERSABLE):
            self.change_direction_vertically(grid)
        # If sparx is moving downward and next point is not traversable
        if self.velocity_y == 1 and (self.y // self.height + 1 >= grid.height or grid.points[self.x // self.width][self.y // self.height + 1].state != TRAVERSABLE):
            self.change_direction_horizontally(grid)
        # If sparx is moving upward and next point is not traversable
        if self.velocity_y == -1 and (self.y // self.height - 1 < 0 or grid.points[self.x // self.width][self.y // self.height - 1].state != TRAVERSABLE):
            self.change_direction_horizontally(grid)

        self.x += self.velocity_x * self.width 
        self.y += self.velocity_y * self.height
