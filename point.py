# States of a point on grid
CLAIMED = 0
UNCLAIMED = 1
TRAVERSABLE = 2
PATH = 3


# Points to be placed on game grid
class Point:
    # Initialize point
    def __init__(self, state) -> None:
        # State of current point
        self.state = state

        # Point size, should be equal to player size (see player.py)
        self.width = 10
        self.height = 10
