from edge import Edge
class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        """src と dest は Node オブジェクトであるとし、weight は数とする"""
        self.src = src
        self.dest = dest
        self.weight = weight

    def get_weight(self):
        return self.weight

    def __str__(self):
        return self.src.get_name() + ' ->(' + str(self.weight) + ') ' + self.dest.get_name()
