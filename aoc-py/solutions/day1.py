"""
Day 1: Historian Hysteria

https://adventofcode.com/2024/day/1
"""
__all__ = ('Day1',)

from typing import ClassVar
from collections import defaultdict

from ..solution import Solution

class Day1(Solution):
    NAME: ClassVar[str] = 'Historian Hysteria'

    def part_one(self, inp: str) -> int:
        list1 = []
        list2 = []

        for line in inp.splitlines():
            a, b = line.split()

            list1.append(int(a))
            list2.append(int(b))

        list1.sort()
        list2.sort()
        return sum(abs(a - b) for a, b in zip(list1, list2))

    def part_two(self, inp: str) -> int:
        list1 = []
        counter = defaultdict(int)

        for line in inp.splitlines():
            a, b = line.split()

            list1.append(int(a))
            counter[int(b)] += 1

        list1.sort()
        return sum(a * counter[a] for a in list1)

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 1319616
        assert p2 == 27267728