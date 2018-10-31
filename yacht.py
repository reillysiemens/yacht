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


def score_ones(dice: List[int]) -> int:
    """ 1 × number of ones """
    return dice.count(1)


def score_twos(dice: List[int]) -> int:
    """ 2 x number of twos """
    return 2 * dice.count(2)


def score_threes(dice: List[int]) -> int:
    """ 3 x number of threes """
    return 3 * dice.count(3)


def score_fours(dice: List[int]) -> int:
    """ 4 × number of fours """
    return 4 * dice.count(4)


def score_fives(dice: List[int]) -> int:
    """ 5 x number of fives """
    return 5 * dice.count(5)


def score_sixes(dice: List[int]) -> int:
    """ 6 x number of sixes """
    return 6 * dice.count(6)


def score_full_house(dice: List[int]) -> int:
    """ Total of the dice """
    dice = sorted(dice)
    full_house = (dice[0] != dice[4] and
                  (dice[0] == dice[1] and dice[2] == dice[3] == dice[4] or
                   dice[3] == dice[4] and dice[0] == dice[1] == dice[2]))
    return sum(dice) if full_house else 0


def score_four_of_a_kind(dice: List[int]) -> int:
    """ Total of the four dice """
    dice = sorted(dice)
    return 4 * dice[3] if dice[0] == dice[3] or dice[1] == dice[4] else 0


def score_little_straight(dice: List[int]) -> int:
    """ 30 points """
    return 30 if sorted(dice) == LITTLE_STRAIGHT else 0


def score_big_straight(dice: List[int]) -> int:
    """ 30 points """
    return 30 if sorted(dice) == BIG_STRAIGHT else 0


def score_choice(dice: List[int]) -> int:
    """ Sum of the dice """
    return sum(dice)


def score_yacht(dice: List[int]) -> int:
    """ 50 points """
    return 50 if all(d == dice[0] for d in dice) else 0


SCORING: Dict[Category, Callable[[List[int]], int]] = {
    Category.ONES: score_ones,
    Category.TWOS: score_twos,
    Category.THREES: score_threes,
    Category.FOURS: score_fours,
    Category.FIVES: score_fives,
    Category.SIXES: score_sixes,
    Category.FULL_HOUSE: score_full_house,
    Category.FOUR_OF_A_KIND: score_four_of_a_kind,
    Category.LITTLE_STRAIGHT: score_little_straight,
    Category.BIG_STRAIGHT: score_big_straight,
    Category.CHOICE: score_choice,
    Category.YACHT: score_yacht,
}


def score(dice: List[int], category: Category) -> int:
    """ Score a sequence of dice rolls based on a given category. """
    return SCORING[category](dice)
