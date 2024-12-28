"""
Day 25: Code Chronicle

https://adventofcode.com/2024/day/25
"""
__all__ = ('Day25',)

from typing import ClassVar

from ..solution import Solution

class Day25(Solution):
    NAME: ClassVar[str] = 'Code Chronicle'

    def part_one(self, inp: str) -> int:
        locks = []
        keys = []

        for schematic in inp.split('\n\n'):
            schematic = schematic.splitlines()
            n_rows = len(schematic)
            n_cols = len(schematic[0])

            # record heights for each key/lock with: counter[i] = height of column `i`
            counter = [0] * n_cols

            for col in range(n_cols):
                counter[col] += sum(schematic[row][col] == '#' for row in range(n_rows))

            if all(c == '#' for c in schematic[0]):
                locks.append(counter)
            else:
                keys.append(counter)

        return sum(
            # lock and key doesnt overlap if for each column their heights add up to less than or equal to 7
            # (height of each grid is 7)
            all(lock_col + key_col <= 7 for lock_col, key_col in zip(lock, key))
            for lock in locks
            for key in keys
        )

    def part_two(self, _: str) -> None:
        """No part 2 for day 25!

        Merry Christmas!
        """

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))

        assert p1 == 3327