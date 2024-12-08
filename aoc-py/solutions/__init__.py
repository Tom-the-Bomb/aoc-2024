__all__ = (
    'SOLUTIONS',
    'Day1',
    'Day2',
    'Day3',
    'Day4',
    'Day5',
    'Day6',
    'Day7',
    'Day8',
    'Day9',
)

from .day1 import Day1
from .day2 import Day2
from .day3 import Day3
from .day4 import Day4
from .day5 import Day5
from .day6 import Day6
from .day7 import Day7
from .day8 import Day8
from .day9 import Day9

from ..solution import Solution

SOLUTIONS: tuple[type[Solution], ...] = (
    Day1,
    Day2,
    Day3,
    Day4,
    Day5,
    Day6,
    Day7,
    Day8,
    Day9,
)

del Solution