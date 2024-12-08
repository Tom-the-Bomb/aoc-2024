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

    def turn_right(self, dr: int, dc: int) -> tuple[int, int]:
        match (dr, dc):
            case (1, 0):
                return 0, -1
            case (-1, 0):
                return 0, 1
            case (0, 1):
                return 1, 0
            case (0, -1):
                return -1, 0
            case _:
                return 0, 0

    def part_one(self, inp: str) -> int:
        grid = inp.splitlines()
        n_rows = len(grid)
        n_cols = len(grid[0])

        row, col = self._find_start(grid)
        dr, dc = -1, 0

        seen = {(row, col)}

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
                match (dr, dc):
                    case (1, 0):
                        dr, dc = 0, -1
                    case (-1, 0):
                        dr, dc = 0, 1
                    case (0, 1):
                        dr, dc = 1, 0
                    case (0, -1):
                        dr, dc = -1, 0
            else:
                seen.add((row, col))

        return len(seen)

    def traverse_line(self, grid: list[str], set1: set, n_rows: int, n_cols: int, row: int, col: int, dr: int, dc: int) -> None:
        row += dr
        col += dc

        if row not in range(n_rows) or col not in range(n_cols) or grid[row][col] == '#':
            return

        set1.add((row, col, -dr, -dc))

        drr, dcc = self.turn_right(dr, dc)

        if row + drr in range(n_rows) and col + dcc in range(n_cols) and grid[row + drr][col + dcc] == '#':
            self.traverse_line(grid, set1, n_rows, n_cols, row, col, -drr, -dcc)
        else:
            self.traverse_line(grid, set1, n_rows, n_cols, row, col, dr, dc)

    def part_two(self, inp: str) -> int:
        grid = inp.splitlines()
        n_rows = len(grid)
        n_cols = len(grid[0])

        row, col = self._find_start(grid)
        dr, dc = -1, 0

        set1 = set()
        seen = [(row, col, dr, dc)]

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
                dr, dc = self.turn_right(dr, dc)

                self.traverse_line(grid, set1, n_rows, n_cols, row, col, dr, dc)
                self.traverse_line(grid, set1, n_rows, n_cols, row, col, -dr, -dc)
            else:
                seen.append((row, col, dr, dc))
            set1.add((row, col, dr, dc))
        total = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if any(x[:2] == (i, j) for x in set1):
                    print('&', end='')
                else:
                    print(cell, end='')
            print()

        for i, (row, col, dr, dc) in enumerate(seen):
            drr, dcc = self.turn_right(dr, dc)
            if (row, col, drr, dcc) in set1 and not any(x[:2] == (row + dr, col + dc) for x in seen[:i]):
                print((row + dr, col + dc))
                total += 1
        return total

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        #assert p1 == 4696
        #assert p2 == 70478672