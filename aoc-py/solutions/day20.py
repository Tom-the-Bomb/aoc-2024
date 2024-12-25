"""
Day 20: Race Condition

https://adventofcode.com/2024/day/20
"""
__all__ = ('Day20',)

from typing import ClassVar
from collections import deque

from ..solution import Solution
from ..utils import find_start, neighbors_4

class Day20(Solution):
    NAME: ClassVar[str] = 'Race Condition'

    def part_one(self, inp: str) -> int:
        grid = inp.splitlines()
        start = find_start(grid, 'S')

        walls = [
            (i, j)
            for i, row in enumerate(grid[1:-1], 1)
            for j, cell in enumerate(row[1:-1], 1)
            if cell == '#'
        ]

        to_check = deque([(*start, 0)])
        seen = {}

        while to_check:
            row, col, dist = to_check.popleft()

            for next_coord in neighbors_4(row, col):
                next_row, next_col = next_coord

                if grid[next_row][next_col] != '#' and next_coord not in seen:
                    to_check.append((*next_coord, dist + 1))
                    seen[next_coord] = dist + 1

        total = 0

        for wall_i, wall_j in walls:
            if (
                grid[wall_i + 1][wall_j] != '#' and grid[wall_i - 1][wall_j] != '#'
                and abs(seen[(wall_i + 1, wall_j)] - seen[(wall_i - 1, wall_j)]) - 2 >= 100
            ) or (
                grid[wall_i][wall_j + 1] != '#' and grid[wall_i][wall_j - 1] != '#'
                and abs(seen[(wall_i, wall_j + 1)] - seen[(wall_i, wall_j - 1)]) - 2 >= 100
            ):
                total += 1

        return total

    def part_two(self, inp: str) -> int:
        grid = inp.splitlines()
        start = find_start(grid, 'S')

        to_check = deque([(*start, 0)])
        seen = {}
        indexed = {}

        while to_check:
            row, col, dist = to_check.popleft()

            for next_coord in neighbors_4(row, col):
                next_row, next_col = next_coord

                if grid[next_row][next_col] != '#' and next_coord not in seen:
                    to_check.append((*next_coord, dist + 1))
                    seen[next_coord] = dist + 1
                    indexed[dist] = next_coord

        for pos in indexed:
            worthReaching = []
            #push all positions 100 away from the current one
            #find all position that are worth reaching and reachable within 20 block radius
            #return all positions

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        #assert p1 == 1647200528
        #assert p2 == 70478672