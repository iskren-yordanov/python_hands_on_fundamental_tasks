"""Helper file containing code for Dice object"""

import random
from datetime import datetime

class Dice():
    """Class Dice"""

    def __init__(self):
        """Dice initialization"""
        random.seed(datetime.today().timestamp())

    def roll(self):
        """Result from rolling a dice"""
        return random.randint(1,6)

    def init_random_generator(self, s: int):
        """Init random generator"""
        random.seed(s)
