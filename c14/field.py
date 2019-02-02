class Field(object):
    def __init__(self):
        self.drunks = {}

    def add_drunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def move_drunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Duplicate drunk')
        x_dist, y_dist = drunk.take_step()
        current_location = self.drunks[drunk]
        self.drunks[drunk] = current_location.move(x_dist, y_dist)

    def get_loc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Duplicate drunk')
        return self.drunks[drunk]