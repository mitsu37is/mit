class Location(object):
    def __init__(self, x, y):
        """x と y は浮動小数点数"""
        self.x, self.y = x, y

    def move(self, delta_x, delta_y):
        """delta_x と delta_y は浮動小数点数"""
        return Location(self.x + delta_x, self.y + delta_y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def dist_from(self, other):
        ox, oy = other.x, other.y
        x_dist, y_dist = self.x -ox, self.y -oy
        return (x_dist**2 + y_dist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
