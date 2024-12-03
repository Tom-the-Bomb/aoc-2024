"""
Day 3: Mull It Over

https://adventofcode.com/2024/day/3
"""
__all__ = ('Day3',)

from typing import ClassVar
import re

from ..solution import Solution

class Day3(Solution):
    NAME: ClassVar[str] = 'Mull It Over'

    def part_one(self, inp: str) -> int:
        return sum(
            int(mul.group(1)) * int(mul.group(2))
            for mul in re.finditer(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', inp)
        )

    def part_two(self, inp: str) -> int:
        total = 0
        do = True

        for mul in re.finditer(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)|do\(\)|don\'t\(\)', inp):
            match mul.group():
                case 'do()':
                    do = True
                case 'don\'t()':
                    do = False
                case _:
                    if do:
                        total += int(mul.group(1)) * int(mul.group(2))
        return total

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 164730528
        assert p2 == 70478672