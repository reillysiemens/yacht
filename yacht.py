from enum import Enum, auto

from typing import List

__version__ = '0.1.0b'


class Category(Enum):
    ONES = auto()
    TWOS = auto()
    THREES = auto()
    FOURS = auto()
    FIVES = auto()
    SIXES = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    LITTLE_STRAIGHT = auto()
    BIG_STRAIGHT = auto()
    CHOICE = auto()
    YACHT = auto()


def score(dice: List, category: Category) -> int:
    """ TODO """
    pass
