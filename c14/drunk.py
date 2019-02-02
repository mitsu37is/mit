class Drunk(object):
    def __init__(self, name=None):
        """name は文字列とする"""
        self.name = name

    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'
