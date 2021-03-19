import pygame
from node import Node


class Player:
    # Initialize Player
    def __init__(self, color, border) -> None:
        # Player color
        self.color = color

        # Player size
        self.radius = 7.5

        # Player current position
        self.x = 400
        self.y = 550

        # Fastest speed at which Player can travel
        self.max_speed = 5

        # Current Player velocity
        self.velocity_x = 0
        self.velocity_y = 0

        # Current nodes that Player is moving between
        self.traversing_nodes = [border.nodes[2], border.nodes[3]]

        # Whether Player can move freely into play field
        self.is_pushing = False

    # Draw Player on screen
    def draw(self, surface) -> None:
        self.move()
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    # Start moving Player on screen
    def start_moving(self, direction_x, direction_y) -> None:
        self.velocity_x = (
            direction_x * self.max_speed) if direction_x != 0 else 0
        self.velocity_y = (
            direction_y * self.max_speed) if direction_y != 0 else 0

    # Stop moving Player on screen
    def stop_moving(self) -> None:
        self.velocity_x = self.velocity_y = 0

    # Move Player
    def move(self) -> None:
        # Clamp Player to current traversing nodes
        if not self.is_pushing:
            self.x = max(self.traversing_nodes[0].x, self.traversing_nodes[1].x
                         ) if self.x > self.traversing_nodes[0].x and self.x > self.traversing_nodes[1].x else self.x
            self.x = min(self.traversing_nodes[0].x, self.traversing_nodes[1].x
                         ) if self.x < self.traversing_nodes[0].x and self.x < self.traversing_nodes[1].x else self.x
            self.y = max(self.traversing_nodes[0].y, self.traversing_nodes[1].y
                         ) if self.y > self.traversing_nodes[0].y and self.y > self.traversing_nodes[1].y else self.y
            self.y = min(self.traversing_nodes[0].y, self.traversing_nodes[1].y
                         ) if self.y < self.traversing_nodes[0].y and self.y < self.traversing_nodes[1].y else self.y

        self.x += self.velocity_x
        self.y += self.velocity_y
