__all__ = (
    'SOLUTIONS',
    'Day1',
    'Day2',
)

from .day1 import Day1
from .day2 import Day2

from ..solution import Solution

SOLUTIONS: tuple[type[Solution], ...] = (
    Day1,
    Day2,
)

del Solution