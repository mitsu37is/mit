class Edge(object):
    def __init__(self, src, dest):
        """src と dest はどちらも Node オブジェクトとする"""
        self.src = src
        self.dest = dest

    def get_src(self):
        return self.src

    def get_destination(self):
        return self.dest

    def __str__(self):
        return self.src.get_name() + 'ー＞' + self.dest.get_name()
