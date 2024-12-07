"""
Day 4: Ceres Search

https://adventofcode.com/2024/day/4
"""
__all__ = ('Day4',)

from typing import ClassVar

from ..solution import Solution

class Day4(Solution):
    NAME: ClassVar[str] = 'Ceres Search'
    DIRECTIONS: ClassVar[tuple[tuple[int, int], ...]] = (
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    )
    CORNERS: ClassVar[set[str]] = {'M', 'S'}

    def _find_xmas(
        self,
        grid: list[str],
        n_rows: int,
        n_cols: int,
        i: int, j: int,
        dr: int, dc: int,
        progression: int,
    ) -> bool:
        if progression == 4:
            return True

        if i not in range(n_rows) or j not in range(n_cols):
            return False

        if grid[i][j] == 'XMAS'[progression]:
            return self._find_xmas(grid, n_rows, n_cols, i + dr, j + dc, dr, dc, progression + 1)
        return False

    def part_one(self, inp: str) -> int:
        grid = inp.splitlines()
        n_rows = len(grid)
        n_cols = len(grid[0])

        total = 0

        for i, row in enumerate(grid):
            for j, letter in enumerate(row):
                # potential start of XMAS chain
                if letter == 'X':
                    for dr, dc in self.DIRECTIONS:
                        total += self._find_xmas(grid, n_rows, n_cols, i, j, dr, dc, 0)
        return total

    def part_two(self, inp: str) -> int:
        grid = inp.splitlines()
        n_cols = len(grid[0])

        total = 0

        for i in range(1, len(grid) - 1):
            for j in range(1, n_cols - 1):
                # potential center of MAS cross
                if grid[i][j] == 'A':
                    tl = grid[i - 1][j - 1]
                    tr = grid[i - 1][j + 1]
                    bl = grid[i + 1][j - 1]
                    br = grid[i + 1][j + 1]

                    total += {tl, br} == self.CORNERS and {tr, bl} == self.CORNERS
        return total

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 2578
        assert p2 == 1972