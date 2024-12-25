"""
Day 19: Linen Layout

https://adventofcode.com/2024/day/19
"""
__all__ = ('Day19',)

from typing import ClassVar
from functools import cache

from ..solution import Solution

class Day19(Solution):
    NAME: ClassVar[str] = 'Linen Layout'

    def _parse_inp(self, inp: str) -> tuple[list[str], list[str]]:
        options, designs = inp.split('\n\n', maxsplit=1)

        return options.split(', '), designs.splitlines()

    def _create(self, design: str, options: list[str]) -> int:
        # optimization: use an inner function
        #
        # reduced cache size as we will not be storing the static un-changing `options` every time in the key
        @cache
        def _create_inner(design: str) -> int:
            if not design:
                # 1 possible way to make the design achieved
                return 1

            ways = 0
            for option in options:
                if design.startswith(option):
                    ways += _create_inner(design[len(option):])
            return ways

        # return the total number of possibilities to make `design` (`0` if not possible)
        return _create_inner(design)

    def part_one(self, inp: str) -> int:
        options, designs = self._parse_inp(inp)

        return sum(
            # only add 1 if each design is creatable (ways greater than 0)
            self._create(design, options) > 0
            for design in designs
        )

    def part_two(self, inp: str) -> int:
        options, designs = self._parse_inp(inp)

        return sum(
            self._create(design, options) for design in designs
        )

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 311
        assert p2 == 616234236468263