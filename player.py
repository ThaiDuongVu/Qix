import pygame
from pygame.locals import *
from grid import Grid
from point import CLAIMED, TRAVERSABLE, UNCLAIMED, PATH


# User-controlled player
class Player:
    # Initialize player
    def __init__(self, color) -> None:
        # Player color
        self.color = color

        # Player current position
        self.x = 240
        self.y = 490

        # Speed at which player will move at
        self.velocity_x = 0
        self.velocity_y = 0

        # Size of player, should be equal to point size (see point.py)
        self.width = 10
        self.height = 10

        self.health = 3

        # Whether player is pushing into board
        self.is_pusing = False
        # Path that player take while pushing in
        self.path = []

    # Player move into a traversable point on grid
    def move_traversable(self, grid: Grid) -> None:
        if len(self.path) > 0:
            # Add point to current path
            self.path.append((self.x, self.y))
            # Set path point state as path
            grid.points[self.x // self.width][self.y //
                                              self.height].state = PATH

        self.x += self.velocity_x * self.width
        self.y += self.velocity_y * self.height

        # If length of path is greater than zero,
        # meaning player moving in from an unclaimed position,
        # perform the following actions
        if len(self.path) > 0:
            # Helper values
            path_start_x = self.path[0][0]
            path_end_x = self.path[len(self.path)-1][0]
            path_start_y = self.path[0][1]
            path_end_y = self.path[len(self.path)-1][1]

            # Each path player takes divides the current grid into 2 halves
            # List of points in each half
            half_1 = []
            half_2 = []

            # Helper functions to add points to half_1 and half_2 lists
            def expand_half_vertically() -> None:
                # Add to path1
                point_to_add = (self.x, self.y)
                while point_to_add != self.path[0]:
                    half_1.append(point_to_add)
                    # Search upward
                    up_point = (point_to_add[0], point_to_add[1] - self.height)
                    if up_point[1] >= 0 and (grid.points[up_point[0] // self.width][up_point[1] // self.height].state == TRAVERSABLE or grid.points[up_point[0] // self.width][up_point[1] // self.height].state == PATH) and up_point not in half_1:
                        point_to_add = up_point
                        continue
                    # Search downward
                    down_point = (point_to_add[0],
                                  point_to_add[1] + self.height)
                    if down_point[1] < grid.height * self.height and (grid.points[down_point[0] // self.width][down_point[1] // self.height].state == TRAVERSABLE or grid.points[down_point[0] // self.width][down_point[1] // self.height].state == PATH) and down_point not in half_1:
                        point_to_add = down_point
                        continue
                    # Search to the left
                    left_point = (point_to_add[0] -
                                  self.width, point_to_add[1])
                    if left_point[0] >= 0 and (grid.points[left_point[0] // self.width][left_point[1] // self.height].state == TRAVERSABLE or grid.points[left_point[0] // self.width][left_point[1] // self.height].state == PATH) and left_point not in half_1:
                        point_to_add = left_point
                        continue
                    # Search to the right
                    right_point = (
                        point_to_add[0] + self.width, point_to_add[1])
                    if right_point[0] < grid.width * self.width and (grid.points[right_point[0] // self.width][right_point[1] // self.height].state == TRAVERSABLE or grid.points[right_point[0] // self.width][right_point[1] // self.height].state == PATH) and right_point not in half_1:
                        point_to_add = right_point
                        continue

                # Add to path2
                point_to_add = (self.x, self.y)
                while point_to_add != self.path[0]:
                    half_2.append(point_to_add)
                    # Search downward
                    down_point = (point_to_add[0],
                                  point_to_add[1] + self.height)
                    if down_point[1] < grid.height * self.height and (grid.points[down_point[0] // self.width][down_point[1] // self.height].state == TRAVERSABLE or grid.points[down_point[0] // self.width][down_point[1] // self.height].state == PATH) and down_point not in half_2:
                        point_to_add = down_point
                        continue
                    # Search upward
                    up_point = (point_to_add[0], point_to_add[1] - self.height)
                    if up_point[1] >= 0 and (grid.points[up_point[0] // self.width][up_point[1] // self.height].state == TRAVERSABLE or grid.points[up_point[0] // self.width][up_point[1] // self.height].state == PATH) and up_point not in half_2:
                        point_to_add = up_point
                        continue
                    # Search to the left
                    left_point = (point_to_add[0] -
                                  self.width, point_to_add[1])
                    if left_point[0] >= 0 and (grid.points[left_point[0] // self.width][left_point[1] // self.height].state == TRAVERSABLE or grid.points[left_point[0] // self.width][left_point[1] // self.height].state == PATH) and left_point not in half_2:
                        point_to_add = left_point
                        continue
                    # Search to the right
                    right_point = (
                        point_to_add[0] + self.width, point_to_add[1])
                    if right_point[0] < grid.width * self.width and (grid.points[right_point[0] // self.width][right_point[1] // self.height].state == TRAVERSABLE or grid.points[right_point[0] // self.width][right_point[1] // self.height].state == PATH) and right_point not in half_2:
                        point_to_add = right_point
                        continue

            def expand_half_horizontally() -> None:
                # Add to path1
                point_to_add = (self.x, self.y)
                while point_to_add != self.path[0]:
                    half_1.append(point_to_add)
                    # Search to the left
                    left_point = (point_to_add[0] -
                                  self.width, point_to_add[1])
                    if left_point[0] >= 0 and (grid.points[left_point[0] // self.width][left_point[1] // self.height].state == TRAVERSABLE or grid.points[left_point[0] // self.width][left_point[1] // self.height].state == PATH) and left_point not in half_1:
                        point_to_add = left_point
                        continue
                    # Search to the right
                    right_point = (
                        point_to_add[0] + self.width, point_to_add[1])
                    if right_point[0] < grid.width * self.width and (grid.points[right_point[0] // self.width][right_point[1] // self.height].state == TRAVERSABLE or grid.points[right_point[0] // self.width][right_point[1] // self.height].state == PATH) and right_point not in half_1:
                        point_to_add = right_point
                        continue
                    # Search upward
                    up_point = (point_to_add[0], point_to_add[1] - self.height)
                    if up_point[1] >= 0 and (grid.points[up_point[0] // self.width][up_point[1] // self.height].state == TRAVERSABLE or grid.points[up_point[0] // self.width][up_point[1] // self.height].state == PATH) and up_point not in half_1:
                        point_to_add = up_point
                        continue
                    # Search downward
                    down_point = (point_to_add[0],
                                  point_to_add[1] + self.height)
                    if down_point[1] < grid.height * self.height and (grid.points[down_point[0] // self.width][down_point[1] // self.height].state == TRAVERSABLE or grid.points[down_point[0] // self.width][down_point[1] // self.height].state == PATH) and down_point not in half_1:
                        point_to_add = down_point
                        continue

                # Add to path2
                point_to_add = (self.x, self.y)
                while point_to_add != self.path[0]:
                    half_2.append(point_to_add)
                    # Search to the right
                    right_point = (
                        point_to_add[0] + self.width, point_to_add[1])
                    if right_point[0] < grid.width * self.width and (grid.points[right_point[0] // self.width][right_point[1] // self.height].state == TRAVERSABLE or grid.points[right_point[0] // self.width][right_point[1] // self.height].state == PATH) and right_point not in half_2:
                        point_to_add = right_point
                        continue
                    # Search to the left
                    left_point = (point_to_add[0] -
                                  self.width, point_to_add[1])
                    if left_point[0] >= 0 and (grid.points[left_point[0] // self.width][left_point[1] // self.height].state == TRAVERSABLE or grid.points[left_point[0] // self.width][left_point[1] // self.height].state == PATH) and left_point not in half_2:
                        point_to_add = left_point
                        continue
                    # Search upward
                    up_point = (point_to_add[0], point_to_add[1] - self.height)
                    if up_point[1] >= 0 and (grid.points[up_point[0] // self.width][up_point[1] // self.height].state == TRAVERSABLE or grid.points[up_point[0] // self.width][up_point[1] // self.height].state == PATH) and up_point not in half_2:
                        point_to_add = up_point
                        continue
                    # Search downward
                    down_point = (point_to_add[0],
                                  point_to_add[1] + self.height)
                    if down_point[1] < grid.height * self.height and (grid.points[down_point[0] // self.width][down_point[1] // self.height].state == TRAVERSABLE or grid.points[down_point[0] // self.width][down_point[1] // self.height].state == PATH) and down_point not in half_2:
                        point_to_add = down_point
                        continue
            
            # Expand half horizontally
            if self.x == path_end_x:
                expand_half_horizontally()
            # Expand half vertically
            if self.y == path_end_y:
                expand_half_vertically()

            # Claim which ever half that is smaller
            if len(half_1) < len(half_2):
                for point in half_1:
                    if point == (self.x, self.y):
                        continue
                    grid.points[point[0] // self.width][point[1] //
                                                        self.height].state = CLAIMED
            else:
                for point in half_2:
                    if point == (self.x, self.y):
                        continue
                    grid.points[point[0] // self.width][point[1] //
                                                        self.height].state = CLAIMED

            for _ in range(grid.width):
                for x in range(grid.width):
                    for y in range(grid.height):
                        if (x > 0 and grid.points[x-1][y].state == CLAIMED and grid.points[x][y].state == UNCLAIMED) or (x < grid.width-1 and grid.points[x+1][y].state == CLAIMED and grid.points[x][y].state == UNCLAIMED) or (y > 0 and grid.points[x][y-1].state == CLAIMED and grid.points[x][y].state == UNCLAIMED) or (y < grid.height-1 and grid.points[x][y+1].state == CLAIMED and grid.points[x][y].state == UNCLAIMED):
                            grid.points[x][y].state = CLAIMED

            # Everything in path should now be traversable
            for point in self.path:
                grid.points[point[0] // self.width][point[1] //
                                                    self.height].state = TRAVERSABLE

            # Update claimed percentage to account for new path
            grid.update_stats()

            # When everything is done, clear the paths and the halves
            self.path = []
            half_1 = []
            half_2 = []

    # Player move into an unclaimed point on grid
    def move_unclaimed(self, grid: Grid) -> None:
        # Add point to current path
        self.path.append((self.x, self.y))
        # Set path point state as path
        grid.points[self.x // self.width][self.y //
                                          self.height].state = PATH

        self.x += self.velocity_x * self.width
        self.y += self.velocity_y * self.height

    # Draw player on game surface
    def draw(self, game_surface, grid: Grid) -> None:
        # Move player on traversable grid if player is not pushing
        if self.velocity_x == 1 and (self.x // self.width) + 1 < grid.width and grid.points[(self.x // self.width) + 1][self.y // self.height].state == TRAVERSABLE:
            self.move_traversable(grid)
        elif self.velocity_x == -1 and (self.x // self.width) - 1 >= 0 and grid.points[(self.x // self.width) - 1][self.y // self.height].state == TRAVERSABLE:
            self.move_traversable(grid)

        if self.velocity_y == 1 and (self.y // self.height) + 1 < grid.height and grid.points[self.x // self.width][(self.y // self.height) + 1].state == TRAVERSABLE:
            self.move_traversable(grid)
        elif self.velocity_y == -1 and (self.y // self.height) - 1 >= 0 and grid.points[self.x // self.width][(self.y // self.height) - 1].state == TRAVERSABLE:
            self.move_traversable(grid)

        # Move player on unclaimed grid if player is pushing
        if self.is_pusing:
            if self.velocity_x == 1 and (self.x // self.width) + 1 < grid.width and grid.points[(self.x // self.width) + 1][self.y // self.height].state == UNCLAIMED:
                self.move_unclaimed(grid)
            elif self.velocity_x == -1 and (self.x // self.width) - 1 >= 0 and grid.points[(self.x // self.width) - 1][self.y // self.height].state == UNCLAIMED:
                self.move_unclaimed(grid)

            if self.velocity_y == 1 and (self.y // self.height) + 1 < grid.height and grid.points[self.x // self.width][(self.y // self.height) + 1].state == UNCLAIMED:
                self.move_unclaimed(grid)
            elif self.velocity_y == -1 and (self.y // self.height) - 1 >= 0 and grid.points[self.x // self.width][(self.y // self.height) - 1].state == UNCLAIMED:
                self.move_unclaimed(grid)

        # Render player object
        pygame.draw.rect(game_surface, self.color, [
                         self.x, self.y, self.width, self.height])
