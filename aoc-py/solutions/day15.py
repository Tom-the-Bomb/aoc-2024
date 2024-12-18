"""
Day 15: Warehouse Woes

https://adventofcode.com/2024/day/15
"""
__all__ = ('Day15',)

from typing import ClassVar

from ..solution import Solution
from ..utils import find_start

class Day15(Solution):
    NAME: ClassVar[str] = 'Warehouse Woes'

    def _gps_sum(self, grid: list[list[str]], box: str) -> int:
        return sum(
            100 * i + j
            for i, row in enumerate(grid)
            for j, cell in enumerate(row)
            if cell == box
        )

    def _push_p1(
        self,
        grid: list[list[str]],
        row: int, col: int,
        dr: int, dc: int,
        to_push: tuple[tuple[int, int, str], ...],
    ) -> None:
        match grid[next_row := row + dr][next_col := col + dc]:
            case 'O':
                self._push_p1(
                    grid,
                    next_row, next_col,
                    dr, dc,
                    ((next_row, next_col, 'O'),) + to_push,
                )
            case '.':
                for i, j, char in to_push:
                    grid[i][j] = '.'
                    grid[i + dr][j + dc] = char

    def _push_p2_x(
        self,
        grid: list[list[str]],
        row: int, col: int,
        dc: int,
        push_start: int,
    ) -> None:
        match grid[row][next_col := col + dc]:
            case '[' | ']':
                self._push_p2_x(
                    grid,
                    row, next_col + dc, dc,
                    push_start,
                )
            case '.':
                grid[row][push_start] = '.'

                span = next_col - push_start
                if dc >= 0:
                    grid[row][push_start + 1:next_col + 1] = list('@' + '[]' * (span // 2))
                else:
                    grid[row][next_col:push_start] = list('[]' * (-span // 2) + '@')

    def _push_p2_y(
        self,
        grid: list[list[str]],
        row: int, col: int,
        dr: int,
        to_push: list[tuple[int, int, str]]
    ) -> bool:
        match grid[next_row := row + dr][col]:
            case '[':
                to_push.append((next_row, col, '['))
                to_push.append((next_row, col + 1, ']'))

                return self._push_p2_y(
                    grid,
                    next_row, col, dr,
                    to_push,
                ) and self._push_p2_y(
                    grid,
                    next_row, col + 1, dr,
                    to_push,
                )
            case ']':
                to_push.append((next_row, col - 1, '['))
                to_push.append((next_row, col, ']'))

                return self._push_p2_y(
                    grid,
                    next_row, col - 1, dr,
                    to_push,
                ) and self._push_p2_y(
                    grid,
                    next_row, col, dr,
                    to_push,
                )
            case '.':
                return True
            case _:
                return False

    def part_one(self, inp: str) -> int:
        grid, directions = inp.split('\n\n')
        grid = [list(row) for row in grid.splitlines()]

        row, col = find_start(grid, '@')

        for direction in directions:
            match direction:
                case '^':
                    dr, dc = -1, 0
                case 'v':
                    dr, dc = 1, 0
                case '<':
                    dr, dc = 0, -1
                case '>':
                    dr, dc = 0, 1
                case _:
                    continue

            self._push_p1(grid, row, col, dr, dc, ((row, col, '@'),))

            if grid[row][col] != '@':
                row += dr
                col += dc

        return self._gps_sum(grid, 'O')

    def part_two(self, inp: str) -> int:
        grid, directions = inp.split('\n\n')
        grid = [
            list(row) for row in grid
                .replace('#', '##')
                .replace('O', '[]')
                .replace('.', '..')
                .replace('@', '@.')
                .splitlines()
        ]
        row, col = find_start(grid, '@')

        for direction in directions:
            match direction:
                case '^':
                    dr, dc = -1, 0
                case 'v':
                    dr, dc = 1, 0
                case '<':
                    dr, dc = 0, -1
                case '>':
                    dr, dc = 0, 1
                case _:
                    continue

            if dr != 0 and self._push_p2_y(grid, row, col, dr, to_push := [(row, col, '@')]):
                pushed = set()

                for i, j, char in reversed(to_push):
                    if (i, j) not in pushed:
                        grid[i][j] = '.'
                        grid[i + dr][j] = char
                        pushed.add((i, j))
            else:
                self._push_p2_x(grid, row, col, dc, col)

            if grid[row][col] != '@':
                row += dr
                col += dc

        return self._gps_sum(grid, '[')

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 1515788
        assert p2 == 1516544