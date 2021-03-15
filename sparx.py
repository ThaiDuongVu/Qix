import pygame


class Sparx:
    def __init__(self, color, init_direction) -> None:
        # Sparx color
        self.color = color

        # Sparx size
        self.radius = 5

        # Sparx current position
        self.x = 400
        self.y = 50

        # Fastest speed at which Sparx can travel
        self.max_speed = 5

        # Current player velocity
        self.velocity_x = 0
        self.velocity_y = 0

        # Initial direction that Sparx will move at, either "right" or "left"
        self.init_direction = init_direction

        # Current nodes that Sparx is moving between
        self.traversing_nodes = []
        self.end_node_index = 0

    # Draw sparx on screen
    def draw(self, surface, border) -> None:
        self.move(border)
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    # Move Sparx along the game border
    def move(self, border) -> None:
        # If reached end node then change current traversing nodes accordingly
        if self.x == self.traversing_nodes[1][0] and self.y == self.traversing_nodes[1][1]:
            self.traversing_nodes[0] = self.traversing_nodes[1]
            if self.init_direction == "right":
                self.end_node_index = self.end_node_index + \
                    1 if self.end_node_index < len(border.nodes) - 1 else 0
            else:
                self.end_node_index = self.end_node_index - \
                    1 if self.end_node_index > 0 else len(border.nodes) - 1

            self.traversing_nodes[1] = border.nodes[self.end_node_index]

        # Set Sparx velocity based on current traversing nodes
        x_gap = self.traversing_nodes[1][0] - self.traversing_nodes[0][0]
        y_gap = self.traversing_nodes[1][1] - self.traversing_nodes[0][1]
        self.velocity_x = x_gap / \
            abs(x_gap) * self.max_speed if x_gap != 0 else 0
        self.velocity_y = y_gap / \
            abs(y_gap) * self.max_speed if y_gap != 0 else 0

        # Move Sparx at x and y position at current velocity
        self.x += self.velocity_x
        self.y += self.velocity_y
