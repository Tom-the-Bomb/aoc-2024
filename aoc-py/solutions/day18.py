"""
Day 18: RAM Run

https://adventofcode.com/2024/day/18
"""
__all__ = ('Day18',)

from typing import ClassVar
import re

from ..solution import Solution

class Day18(Solution):
    NAME: ClassVar[str] = 'RAM Run'

    def part_one(self, inp: str) -> int:
        ...

    def part_two(self, inp: str) -> int:
        ...

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        #assert p1 == 1647180528
        #assert p2 == 70478672