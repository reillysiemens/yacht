from enum import Enum, auto

from typing import Callable, Dict, List

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


def _score_ones(dice: List[int]) -> int:
    """ TODO """
    pass


def _score_twos(dice: List[int]) -> int:
    """ TODO """
    pass


def _score_threes(dice: List[int]) -> int:
    """ TODO """
    pass


def _score_fours(dice: List[int]) -> int:
    """ TODO """
    pass


def _score_fives(dice: List[int]) -> int:
    """ TODO """
    pass


def _score_sixes(dice: List[int]) -> int:
    """ TODO """
    pass


def _score_full_house(dice: List[int]) -> int:
    """ TODO """
    pass


def _score_four_of_a_kind(dice: List[int]) -> int:
    """ TODO """
    pass


def _score_little_straight(dice: List[int]) -> int:
    """ TODO """
    pass


def _score_big_straight(dice: List[int]) -> int:
    """ TODO """
    pass


def _score_choice(dice: List[int]) -> int:
    """ TODO """
    pass


def _score_yacht(dice: List[int]) -> int:
    """ TODO """
    pass


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
