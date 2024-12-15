"""
Day 15: Warehouse Woes

https://adventofcode.com/2024/day/15
"""
__all__ = ('Day15',)

from typing import ClassVar

from ..solution import Solution

class Day15(Solution):
    NAME: ClassVar[str] = 'Warehouse Woes'

    def part_one(self, inp: str) -> int:
        grid = inp.splitlines()

    def part_two(self, inp: str) -> int:
        ...

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        #assert p1 == 1647150528
        #assert p2 == 70478672