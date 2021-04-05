import pygame
from pygame.locals import *
from point import CLAIMED, Point, TRAVERSABLE, UNCLAIMED


# Grid for player to move on
class Grid:
    # Initialize grid
    def __init__(self, width, height, claimed_color, unclaimed_color, traversable_color, path_color) -> None:
        # Width and height of grid
        self.width = width
        self.height = height

        self.unclaimed_points = 0
        self.claimed_points = 0
        # Percentage of claimed points on grid
        self.claimed_percent = 0

        # Place points on grid
        # 2D array with x and y coordinates of each point
        self.points = [[Point(UNCLAIMED) for i in range(self.width)]
                       for j in range(self.height)]

        # Set edge points to be traversable by player
        for x in range(self.width):
            self.points[x][0].state = self.points[x][self.height -
                                                     1].state = TRAVERSABLE
        for y in range(self.height):
            self.points[0][y].state = self.points[self.width -
                                                  1][y].state = TRAVERSABLE

        # Colors for different points
        self.claimed_color = claimed_color
        self.unclaimed_color = unclaimed_color
        self.traversable_color = traversable_color
        self.path_color = path_color

    # Draw grid of game surface
    def draw(self, game_surface) -> None:
        for x in range(self.width):
            for y in range(self.height):
                point = self.points[x][y]
                if point.state == UNCLAIMED:
                    pygame.draw.rect(game_surface, self.unclaimed_color, [
                                     x * point.width, y * point.height, point.width, point.height])
                elif point.state == CLAIMED:
                    pygame.draw.rect(game_surface, self.claimed_color, [
                                     x * point.width, y * point.height, point.width, point.height])
                elif point.state == TRAVERSABLE:
                    pygame.draw.rect(game_surface, self.traversable_color, [
                                     x * point.width, y * point.height, point.width, point.height])
                else:
                    pygame.draw.rect(game_surface, self.path_color, [
                        x * point.width, y * point.height, point.width, point.height])

    # Update claimed percentage
    def update_stats(self) -> None:
        self.claimed_points = 0
        self.unclaimed_points = 0
        for x in range(self.width):
            for y in range(self.height):
                point = self.points[x][y]
                if point.state == CLAIMED:
                    self.claimed_points += 1
                elif point.state == UNCLAIMED:
                    self.unclaimed_points += 1

        self.claimed_percent = (self.claimed_points /
                                (self.unclaimed_points + self.claimed_points)) * 100
