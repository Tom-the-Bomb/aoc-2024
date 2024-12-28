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

    def _build_path(self, grid: list[str]) -> dict[tuple[int, int], int]:
        start = find_start(grid, 'S')

        to_check = deque([(*start, 0)])
        path = {start: 0}

        while to_check:
            row, col, dist = to_check.popleft()

            for next_coord in neighbors_4(row, col):
                next_row, next_col = next_coord

                if grid[next_row][next_col] != '#' and next_coord not in path:
                    to_check.append((*next_coord, dist + 1))
                    path[next_coord] = dist + 1

        # builds a map of every location along the path -> the distance it takes to travel there from the start (`S`)
        return path

    def part_one(self, inp: str) -> int:
        grid = inp.splitlines()
        walls = [
            (i, j)
            for i, row in enumerate(grid[1:-1], 1)
            for j, cell in enumerate(row[1:-1], 1)
            if cell == '#'
        ]

        path = self._build_path(grid)
        total = 0

        # A 2 picosecond cheat is basiclly limited to jumping over a wall:
        # check all walls we could jump over
        for wall_i, wall_j in walls:
            if (
                # jump over a wall from the `bottom`` to the `top` (UP and DOWN neighbors are not walls)
                grid[wall_i + 1][wall_j] != '#' and grid[wall_i - 1][wall_j] != '#'
                # abs(...) calculates the original distance needed to traverse to get from top to bottom (either way)
                #
                # the time saved will be that *minus* `2` as 2 picoseconds is the new time needed to simply just jump over the wall: `.` -> '#' -> '.'
                and abs(path[(wall_i + 1, wall_j)] - path[(wall_i - 1, wall_j)]) - 2 >= 100
            ) or (
                # same thing but for jumping over a wall from the left to the right
                grid[wall_i][wall_j + 1] != '#' and grid[wall_i][wall_j - 1] != '#'
                and abs(path[(wall_i, wall_j + 1)] - path[(wall_i, wall_j - 1)]) - 2 >= 100
            ):
                total += 1

        return total

    def part_two(self, inp: str) -> int:
        grid = inp.splitlines()
        path = self._build_path(grid)

        total = 0

        for (start_i, start_j), start_dist in path.items():
            for radius in range(2, 21):
                for dr in range(radius + 1):
                    # manhattan distance must equal to `radius`: |dr| + |dc| = radius, but `dr` and `dc` currently are both positive already
                    dc = radius - dr

                    # this loop (adding signage) combined with the outer loop: `for dr in range(radius + 1)`
                    # will manage to loop through all possible end positions of the cheat that have a manhattan distance of `radius` away from `start`
                    # (diamond shape)
                    #
                    # meaning they will take `radius` picoseconds to get to from the start position
                    # where radius is all values within [2, 20] picoseconds to test for
                    #
                    # if `dr = dc = 0` then there will be duplicates, that's why we use a `set` not a traditional `tuple`
                    for end_i, end_j in {
                        (start_i - dr, start_j - dc),
                        (start_i - dr, start_j + dc),
                        (start_i + dr, start_j - dc),
                        (start_i + dr, start_j + dc),
                    }:
                        if (
                            (end_dist := path.get((end_i, end_j))) is not None
                            # `end_dist - start_dist` = original distance to go from start -> end (direction matters)
                            # `radius` = new distance after cheating for `radius` picoseconds
                            and end_dist - start_dist - radius >= 100
                        ):
                            total += 1
        return total

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 1197
        assert p2 == 944910