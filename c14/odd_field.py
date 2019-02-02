import random
from location import Location
from field import Field

class oddField(Field):
    def __init__(self, num_holes, x_range, y_range):
        Field.__init__(self)
        self.wormholes = {}
        for w in range(num_holes):
            x = random.randint(-x_range, x_range)
            y = random.randint(-y_range, y_range)
            new_x = random.randint(-x_range, x_range)
            new_y = random.randint(-y_range, y_range)
            new_loc = Location(new_x, new_y)
            self.wormholes[(x, y)] = new_loc

    def move_drunk(self, drunk):
        Field.move_drunk(self, drunk)
        x = self.drunks[drunk].get_x()
        y = self.drunks[drunk].get_y()
        if (x, y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x, y)]