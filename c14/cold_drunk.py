import random
from drunk import Drunk

class ColdDrunk(Drunk):
    def take_step(self):
        step_choices = [(0.0, 1.0), (0.0, -2.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(step_choices)
