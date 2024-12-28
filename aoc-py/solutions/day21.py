"""
Day 21: Keypad Conundrum

https://adventofcode.com/2024/day/21
"""
__all__ = ('Day21',)

from typing import ClassVar
from enum import Enum

from ..solution import Solution

class NumPad(Enum):
    N7 = 0, 0
    N8 = 0, 1
    N9 = 0, 2
    N4 = 1, 0
    N5 = 1, 1
    N6 = 1, 2
    N1 = 2, 0
    N2 = 2, 1
    N3 = 2, 2
    N0 = 3, 1
    A = 3, 2

class DirPad(Enum):
    UP = 0, 1
    A = 0, 2
    LEFT = 1, 0
    DOWN = 1, 1
    RIGHT = 1, 2

class Day21(Solution):
    NAME: ClassVar[str] = 'Keypad Conundrum'

    def part_one(self, inp: str) -> int:
        total = 0

        for passcode in inp.splitlines():
            num_pad = NumPad.A
            dir_pad_1 = DirPad.A
            dir_pad_2 = DirPad.A

        return total

    def part_two(self, inp: str) -> int:
        ...

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        #assert p1 == 1647210528
        #assert p2 == 70478672