"""
Day 12: Garden Groups

https://adventofcode.com/2024/day/12
"""
__all__ = ('Day12',)

from typing import ClassVar
from collections import deque

from ..solution import Solution

class Day12(Solution):
    NAME: ClassVar[str] = 'Garden Groups'

    def part_one(self, inp: str) -> int:
        grid = inp.splitlines()
        n_rows = len(grid)
        n_cols = len(grid[0])

        seen = set()
        total = 0

        for start_i, row in enumerate(grid):
            for start_j, cell in enumerate(row):
                if (start_i, start_j) not in seen:

                    to_check = deque([(start_i, start_j)])
                    local_seen = {(start_i, start_j)}

                    perimeter = 0

                    while to_check:
                        i, j = to_check.popleft()
                        perimeter += 4

                        for next_i, next_j in (
                            (i, j - 1),
                            (i, j + 1),
                            (i - 1, j),
                            (i + 1, j),
                        ):
                            # no side: neighbor is a cell that is part of the garden
                            if (
                                next_i in range(n_rows)
                                and next_j in range(n_cols)
                                and grid[next_i][next_j] == cell
                            ):
                                if (next_c := (next_i, next_j)) not in local_seen:
                                    to_check.append(next_c)
                                    local_seen.add(next_c)

                                perimeter -= 1

                    total += perimeter * len(local_seen)
                    seen |= local_seen
        return total

    def part_two(self, inp: str) -> int:
        grid = inp.splitlines()
        n_rows = len(grid)
        n_cols = len(grid[0])

        seen = set()
        total = 0

        for start_i, row in enumerate(grid):
            for start_j, cell in enumerate(row):
                if (start_i, start_j) not in seen:

                    to_check = deque([(start_i, start_j)])
                    local_seen = {(start_i, start_j)}

                    corners = 0

                    while to_check:
                        i, j = to_check.popleft()

                        for next_i, next_j in (
                            (i, j - 1),
                            (i, j + 1),
                            (i - 1, j),
                            (i + 1, j),
                        ):
                            if (
                                next_i in range(n_rows)
                                and next_j in range(n_cols)
                                and grid[next_i][next_j] == cell
                                and (next_c := (next_i, next_j)) not in local_seen
                            ):
                                to_check.append(next_c)
                                local_seen.add(next_c)

                        for dr, dc in (
                            (-1, -1), (-1, 1), (1, -1), (1, 1),
                        ):
                            side1_exists = (adj_i := i + dr) in range(n_rows)
                            side2_exists = (adj_j := j + dc) in range(n_rows)

                            if (
                                # convex corner: 2 adjacent neighbors do not exist
                                # ....
                                # XE..
                                # .X.. => then the `E` has a convex corner (where . is any character and `X` is not an `E`)
                                (not side1_exists or grid[adj_i][j] != cell)
                                and (not side2_exists or grid[i][adj_j] != cell)
                            ) or (
                                # concave corner: 2 adjacent neighbors do exist and the bounded diagonal does not exist
                                # ....
                                # EE..
                                # XE.. => then the `E` (at row 2, col 2) has a concave corner
                                side1_exists
                                and side2_exists
                                and grid[adj_i][j] == grid[i][adj_j] == cell and grid[adj_i][adj_j] != cell
                            ):
                                corners += 1

                    # the # of corners is equal to the # of sides in a polygon
                    total += corners * len(local_seen)
                    seen |= local_seen
        return total

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 1375574
        assert p2 == 830566