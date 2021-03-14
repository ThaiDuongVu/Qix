import pygame


class PLayer:
    # Initialize player
    def __init__(self, color) -> None:
        # PLayer color
        self.color = color

        # Player size
        self.radius = 7.5

        # Player current position
        self.x = 400
        self.y = 550

        # Fastest speed at which player can travel
        self.max_speed = 5

        # Current player velocity
        self.velocity_x = 0
        self.velocity_y = 0

        # Current nodes that player is moving between
        self.traversing_nodes = []

        # Whether player can move freely into play field
        self.is_pushing = False

        # Current score
        self.score = 0

    # Draw player on screen
    def draw(self, surface) -> None:
        self.move()
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    # Start moving player on screen
    def start_moving(self, direction_x, direction_y) -> None:
        self.velocity_x = (
            direction_x * self.max_speed) if direction_x != 0 else 0
        self.velocity_y = (
            direction_y * self.max_speed) if direction_y != 0 else 0

    # Stop moving player on screen
    def stop_moving(self) -> None:
        self.velocity_x = self.velocity_y = 0

    # Move player
    def move(self) -> None:
        # Clamp player to current traversing nodes
        if not self.is_pushing:
            if self.x > self.traversing_nodes[0][0] and self.x > self.traversing_nodes[1][0]:
                self.x = max(
                    self.traversing_nodes[0][0], self.traversing_nodes[1][0])
            if self.x < self.traversing_nodes[0][0] and self.x < self.traversing_nodes[1][0]:
                self.x = min(
                    self.traversing_nodes[0][0], self.traversing_nodes[1][0])
            if self.y > self.traversing_nodes[0][1] and self.y > self.traversing_nodes[1][1]:
                self.y = max(
                    self.traversing_nodes[0][1], self.traversing_nodes[1][1])
            if self.y < self.traversing_nodes[0][1] and self.y < self.traversing_nodes[1][1]:
                self.y = min(
                    self.traversing_nodes[0][1], self.traversing_nodes[1][1])

        self.x += self.velocity_x
        self.y += self.velocity_y
