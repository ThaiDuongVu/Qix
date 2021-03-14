import pygame


class Border:
    # Initialize game border
    def __init__(self, color) -> None:
        # Border color
        self.color = color

        # Border thickness
        self.thickness = 1

        # List of border nodes
        # Each node is a tuple containing the x and y coordinates
        self.nodes = [(150, 50), (650, 50), (650, 550), (150, 550)]

    # Draw border on screen
    def draw(self, surface) -> None:
        pygame.draw.lines(surface, self.color, True,
                          self.nodes, width=self.thickness)
