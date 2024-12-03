"""
Day 2: Red-Nosed Reports

https://adventofcode.com/2024/day/2
"""
__all__ = ('Day2',)

from typing import ClassVar

from ..solution import Solution

class Day2(Solution):
    NAME: ClassVar[str] = 'Red-Nosed Reports'

    def part_one(self, inp: str) -> int:
        count = 0

        for line in inp.splitlines():
            report = [int(level) for level in line.split()]
            increasing = True

            for i in range(len(report) - 1):
                jump = report[i + 1] - report[i]

                if i == 0:
                    increasing = jump > 0
                if (jump if increasing else -jump) not in range(1, 4):
                    break
            else:
                count += 1
        return count

    def part_two(self, inp: str) -> int:
        count = 0

        for line in inp.splitlines():
            report = [int(level) for level in line.split()]

            n = len(report)

            # test all possible levels to remove
            for remove in range(n):
                new_report = report[:remove] + report[remove + 1:]
                increasing = True

                for i in range(n - 2):
                    jump = new_report[i + 1] - new_report[i]

                    if i == 0:
                        increasing = jump > 0
                    if (jump if increasing else -jump) not in range(1, 4):
                        break
                else:
                    count += 1
                    break
        return count

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 585
        assert p2 == 626