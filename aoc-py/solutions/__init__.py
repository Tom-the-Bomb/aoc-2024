__all__ = (
    'SOLUTIONS',
    'Day1',
    'Day2',
    'Day3',
    'Day4',
    'Day5',
)

from .day1 import Day1
from .day2 import Day2
from .day3 import Day3
from .day4 import Day4
from .day5 import Day5

from ..solution import Solution

SOLUTIONS: tuple[type[Solution], ...] = (
    Day1,
    Day2,
    Day3,
    Day4,
    Day5,
)

del Solution