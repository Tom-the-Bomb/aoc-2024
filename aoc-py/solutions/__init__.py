__all__ = (
    'SOLUTIONS',
    'Day1',
)

from .day1 import Day1

from ..solution import Solution

SOLUTIONS: tuple[type[Solution], ...] = (
    Day1,
)

del Solution