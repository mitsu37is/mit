class Node(object):
    def __init__(self, name):
        """name は文字列とする"""
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name