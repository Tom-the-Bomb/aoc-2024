"""
Day 7: Bridge Repair

https://adventofcode.com/2024/day/7
"""
__all__ = ('Day7',)

from typing import ClassVar, Callable
from math import log10

from ..solution import Solution

class Day7(Solution):
    NAME: ClassVar[str] = 'Bridge Repair'

    def _solve_p1(self, target: int, terms: list[int], curr: int, progression: int) -> bool:
        if progression == len(terms):
            return target == curr

        term = terms[progression]

        return self._solve_p1(
            target,
            terms,
            curr + term,
            progression + 1,
        ) or self._solve_p1(
            target,
            terms,
            curr * term,
            progression + 1,
        )

    def _solve_p2(self, target: int, terms: list[int], curr: int, progression: int) -> bool:
        if progression == len(terms):
            return target == curr

        term = terms[progression]

        return self._solve_p2(
            target,
            terms,
            curr + term,
            progression + 1,
        ) or self._solve_p2(
            target,
            terms,
            curr * term,
            progression + 1,
        ) or self._solve_p2(
            target,
            terms,
            # `int(log10(term)) + 1` gives us the # of digits in the integer: `term`
            curr * 10 ** (int(log10(term)) + 1) + term,
            progression + 1,
        )

    def _solve(self, inp: str, solve_func: Callable[[int, list[int], int, int], bool]) -> int:
        total = 0

        for equation in inp.splitlines():
            target, terms = equation.split(':')

            first, *terms = [int(term) for term in terms.split()]
            target = int(target)

            if solve_func(target, terms, first, 0):
                total += target
        return total

    def part_one(self, inp: str) -> int:
        return self._solve(inp, self._solve_p1)

    def part_two(self, inp: str) -> int:
        return self._solve(inp, self._solve_p2)

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 3351424677624
        assert p2 == 204976636995111