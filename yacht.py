from enum import Enum, auto

from typing import Callable, Dict, List

__version__ = '0.1.0b'

LITTLE_STRAIGHT = [1, 2, 3, 4, 5]
BIG_STRAIGHT = [2, 3, 4, 5, 6]


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


def _score_ones(dice: List[int]) -> int:
    """ 1 × number of ones """
    return dice.count(1)


def _score_twos(dice: List[int]) -> int:
    """ 2 x number of twos """
    return 2 * dice.count(2)


def _score_threes(dice: List[int]) -> int:
    """ 3 x number of threes """
    return 3 * dice.count(3)


def _score_fours(dice: List[int]) -> int:
    """ 4 × number of fours """
    return 4 * dice.count(4)


def _score_fives(dice: List[int]) -> int:
    """ 5 x number of fives """
    return 5 * dice.count(5)


def _score_sixes(dice: List[int]) -> int:
    """ 6 x number of sixes """
    return 6 * dice.count(6)


def _score_full_house(dice: List[int]) -> int:
    """ TODO """
    pass


def _score_four_of_a_kind(dice: List[int]) -> int:
    """ Total of the four dice """
    dice = sorted(dice)
    return 4 * dice[3] if dice[0] == dice[3] or dice[1] == dice[4] else 0


def _score_little_straight(dice: List[int]) -> int:
    """ 30 points """
    return 30 if sorted(dice) == LITTLE_STRAIGHT else 0


def _score_big_straight(dice: List[int]) -> int:
    """ 30 points """
    return 30 if sorted(dice) == BIG_STRAIGHT else 0


def _score_choice(dice: List[int]) -> int:
    """ Sum of the dice """
    return sum(dice)


def _score_yacht(dice: List[int]) -> int:
    """ 50 points """
    return 50 if all(d == dice[0] for d in dice) else 0


_scoring: Dict[Category, Callable[[List[int]], int]] = {
    Category.ONES: _score_ones,
    Category.TWOS: _score_twos,
    Category.THREES: _score_threes,
    Category.FOURS: _score_fours,
    Category.FIVES: _score_fives,
    Category.SIXES: _score_sixes,
    Category.FULL_HOUSE: _score_full_house,
    Category.FOUR_OF_A_KIND: _score_four_of_a_kind,
    Category.LITTLE_STRAIGHT: _score_little_straight,
    Category.BIG_STRAIGHT: _score_big_straight,
    Category.CHOICE: _score_choice,
    Category.YACHT: _score_yacht,
}


def score(dice: List[int], category: Category) -> int:
    """ TODO """
    return _scoring[category](dice)
