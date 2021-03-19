import pygame
from node import Node


class Border:
    # Initialize game border
    def __init__(self, color) -> None:
        # Border color
        self.color = color

        # Border thickness
        self.thickness = 1

        # List of border nodes
        # Each node is a Node containing the x and y coordinates
        self.nodes = [Node(150, 50), Node(650, 50), Node(650, 550), Node(150, 550)]

        # List of border lines to draw
        self.lines = []

    # Draw border on screen
    def draw(self, surface) -> None:
        self.lines = [(node.x, node.y) for node in self.nodes]
        pygame.draw.lines(surface, self.color, True,
                          self.lines, width=self.thickness)
