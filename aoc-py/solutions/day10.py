"""
Day 10: Hoof It

https://adventofcode.com/2024/day/10
"""
__all__ = ('Day10',)

from typing import ClassVar
from collections import deque

from ..solution import Solution
from ..utils import neighbors_4

class Day10(Solution):
    NAME: ClassVar[str] = 'Hoof It'

    def part_one(self, inp: str) -> int:
        grid = inp.splitlines()
        n_rows = len(grid)
        n_cols = len(grid[0])

        count = 0

        for start_i, row in enumerate(grid):
            for start_j, cell in enumerate(row):
                if cell == '0':

                    to_check = deque([(start_i, start_j, 0)])
                    nines = set()

                    while to_check:
                        i, j, num = to_check.popleft()

                        if num == 9:
                            nines.add((i, j))
                        else:
                            for next_i, next_j in neighbors_4(i, j):
                                if (
                                    next_i in range(n_rows)
                                    and next_j in range(n_cols)
                                    and int(grid[next_i][next_j]) == (next_num := num + 1)
                                ):
                                    to_check.append((next_i, next_j, next_num))
                    count += len(nines)
        return count

    def part_two(self, inp: str) -> int:
        grid = inp.splitlines()
        n_rows = len(grid)
        n_cols = len(grid[0])

        count = 0

        for start_i, row in enumerate(grid):
            for start_j, cell in enumerate(row):
                if cell == '0':

                    to_check = deque([(start_i, start_j, 0)])

                    while to_check:
                        i, j, num = to_check.popleft()

                        if num == 9:
                            count += 1
                        else:
                            for next_i, next_j in neighbors_4(i, j):
                                if (
                                    next_i in range(n_rows)
                                    and next_j in range(n_cols)
                                    and int(grid[next_i][next_j]) == (next_num := num + 1)
                                ):
                                    to_check.append((next_i, next_j, next_num))
        return count

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 430
        assert p2 == 928