"""
Day 13: Claw Contraption

https://adventofcode.com/2024/day/13
"""
__all__ = ('Day13',)

from typing import ClassVar
import re

from ..solution import Solution

class Day13(Solution):
    NAME: ClassVar[str] = 'Claw Contraption'

    def _solve(self, inp: str, target_offset: int = 0) -> int:
        total = 0

        machines = map(
            lambda machine: map(int, machine),
            re.findall(
                r'Button A: X\+([0-9]+), Y\+([0-9]+)\n'
                r'Button B: X\+([0-9]+), Y\+([0-9]+)\n'
                r'Prize: X=([0-9]+), Y=([0-9]+)',
                inp,
            )
        )

        for ax, ay, bx, by, target_x, target_y in machines:
            target_x += target_offset
            target_y += target_offset

            # system of linear equations:
            #
            # [1]: ax * a_presses + bx * b_presses = target_x
            # [2]: ay * a_presses + by * b_presses = target_y
            #
            # eliminate `a_presses`:
            #
            #   ([1] * ay): ay * ax * a_presses + ay * bx * b_presses = ay * target_x
            # - ([2] * ax): ax * ay * a_presses + ax * by * b_presses = ax * target_y
            # ---------------------------------------------------------------------
            # =           : (ay * bx - ax * by) * b_presses = ay * target_x - ax * target_y
            # solve for `b_presses`:
            #             : b_presses = (ay * target_x - ax * target_y) / (ay * bx - ax * by)
            #
            # substitute the value of `b_presses` back into [1] and solve for `a_presses`:
            #
            # from [1]: a_presses = (target_x - bx * b_presses) / ax
            b_presses = (ay * target_x - ax * target_y) / (ay * bx - ax * by)
            a_presses = (target_x - bx * b_presses) / ax

            a_presses = round(a_presses)
            b_presses = round(b_presses)

            if ax * a_presses + bx * b_presses == target_x and ay * a_presses + by * b_presses == target_y:
                total += 3 * a_presses + b_presses

        return total

    def part_one(self, inp: str) -> int:
        return self._solve(inp)

    def part_two(self, inp: str) -> int:
        return self._solve(inp, 10000000000000)

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 39996
        assert p2 == 73267584326867