"""
Day 6: Guard Gallivant

https://adventofcode.com/2024/day/6
"""
__all__ = ('Day6',)

from typing import ClassVar

from ..solution import Solution

class Day6(Solution):
    NAME: ClassVar[str] = 'Guard Gallivant'

    def _find_start(self, grid: list[str]) -> tuple[int, int]:
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '^':
                    return i, j
        raise ValueError("No '^' character found in grid")

    def _turn_right(self, dr: int, dc: int) -> tuple[int, int]:
        match dr, dc:
            case 1, 0:
                return 0, -1
            case -1, 0:
                return 0, 1
            case 0, 1:
                return 1, 0
            case 0, -1:
                return -1, 0
            case _:
                raise ValueError('Non-orthogonal direction provided')

    def _get_path(
        self,
        grid: list[str],
        n_rows: int,
        n_cols: int,
        start: tuple[int, int],
    ) -> set[tuple[int, int]]:
        row, col = start
        dr, dc = -1, 0

        seen = {start}

        while True:
            row += dr
            col += dc

            # guard has exited the area
            if row not in range(n_rows) or col not in range(n_cols):
                break

            if grid[row][col] == '#':
                # backtrack upon hitting obstacle
                row -= dr
                col -= dc

                # turn 90 degrees right
                dr, dc = self._turn_right(dr, dc)
            else:
                seen.add((row, col))
        return seen

    def part_one(self, inp: str) -> int:
        grid = inp.splitlines()
        start = self._find_start(grid)

        n_rows = len(grid)
        n_cols = len(grid[0])

        return len(self._get_path(grid, n_rows, n_cols, start))

    def part_two(self, inp: str) -> int:
        grid = inp.splitlines()
        start = self._find_start(grid)

        n_rows = len(grid)
        n_cols = len(grid[0])

        total = 0

        # check all potential placements for obstacles along the guard's traversed path
        for obstacle in self._get_path(grid, n_rows, n_cols, start):
            row, col = start
            dr, dc = -1, 0

            seen = {(row, col, dr, dc)}

            while True:
                row += dr
                col += dc

                if (row, col, dr, dc) in seen:
                    # adding the obstacle created a loop
                    total += 1
                    break

                if row not in range(n_rows) or col not in range(n_cols):
                    break

                if grid[row][col] == '#' or (row, col) ==  obstacle:
                    row -= dr
                    col -= dc

                    dr, dc = self._turn_right(dr, dc)
                else:
                    seen.add((row, col, dr, dc))
        return total

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 4696
        assert p2 == 1443