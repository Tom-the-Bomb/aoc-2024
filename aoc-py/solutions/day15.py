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

    def _push_p2_x(
        self,
        grid: list[list[str]],
        row: int, col: int,
        dc: int,
        push_start: int,
    ) -> None:
        match grid[row][next_col := col + dc]:
            # encountered box
            case '[' | ']':
                self._push_p2_x(
                    grid,
                    # skip over the 2nd half of the box (next_col + dc) and try to find empty space: '.' or new box: '[' | ']'
                    row, next_col + dc, dc,
                    # index of the lanternfish originally
                    push_start,
                )
            # found empty space to push everything we've accumulated into
            #
            # `next_col` is the index of the empty space: '.'
            case '.':
                grid[row][push_start] = '.'

                # rightwards '>' pushing
                if (span := next_col - push_start) >= 0:
                    # pushed onto: right after lanternfish -> empty space: [push_start + 1, next_col]
                    grid[row][push_start + 1:next_col + 1] = '@' + '[]' * (span // 2)
                # leftwards '<' pushing
                else:
                    # pushed onto: empty space -> right before lanternfish: [next_col, push_start -1]
                    grid[row][next_col:push_start] = '[]' * (-span // 2) + '@'

    def _push_p2_y(
        self,
        grid: list[list[str]],
        row: int, col: int,
        dr: int,
        to_push: list[tuple[int, int, str]]
    ) -> bool:
        match grid[next_row := row + dr][col]:
            # left side of box needs to be pushed
            case '[':
                # add box to `to_push` array so we can push if all checks pass
                to_push.append((next_row, col, '['))
                to_push.append((next_row, col + 1, ']'))

                # check if able to be pushed:
                #
                # - check if left (current) side will push more boxes (recursively ...)
                #   (case '[' and case ']' in our match)
                # OR finally is able to be pushed
                #   (case '.' and case _: in our match)
                #
                # [and] (both of these sides need to be able to be pushed for the entire box to be pushed)
                #
                # - check if right (col + 1) side will push more boxes (recursively) OR is able to be pushed
                #
                return self._push_p2_y(
                    grid,
                    next_row, col, dr,
                    to_push,
                ) and self._push_p2_y(
                    grid,
                    next_row, col + 1, dr,
                    to_push,
                )
            # repeat above for if we are currently trying to push the left side of the box
            case ']':
                # left side (col - 1)
                to_push.append((next_row, col - 1, '['))
                # right side (current)
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
            # found empty space for previous box to push onto
            case '.':
                return True
            # hit wall: cannot push
            case _:
                return False

    def part_one(self, inp: str) -> int:
        grid, directions = inp.split('\n\n', maxsplit=1)
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

            next_row = row
            next_col = col

            # try to find empty spot to push everything onto
            while (cell := grid[next_row := next_row + dr][next_col := next_col + dc]) != '.':
                # hit wall but have not found empty spot: cannot push at all
                if cell == '#':
                    break
            else:
                # found empty spot to push onto
                # original lanternfish spot => empty
                grid[row][col] = '.'
                # next spot in path => lanternfish
                grid[row + dr][col + dc] = '@'

                # if the '.' was found more than `1` spot away (`row + dr` or `col + dc`) from the original lanternfish spot:
                #
                # this means there were 1 or more boxes in between
                if next_row != row + dr or next_col != col + dc:
                    grid[next_row][next_col] = 'O'

            # lanternfish was moved: update `(row, col)` position tracker
            if grid[row][col] != '@':
                row += dr
                col += dc

        return self._gps_sum(grid, 'O')

    def part_two(self, inp: str) -> int:
        grid, directions = inp.split('\n\n', maxsplit=1)
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

            # dr != 0 => vertical pushing
            # the result of `_push_py_2(...)` tells us if we are able to push at all
            #
            if dr != 0 and self._push_p2_y(grid, row, col, dr, to_push := [(row, col, '@')]):
                # redundant pushes are found in `to_push`
                pushed = set()

                # (i, j) => original location of `char` that needs to be pushed in `dr` direction vertically
                #
                # `to_push` is stored as: closer to lanternfish to further away
                # but we want to push the ones furthest from lanternfish away first so we don't overwrite previous pushes with '.'
                #
                # hence use `reversed(...)`
                for i, j, char in reversed(to_push):
                    # do not push redundantly or pushed characters will be overwritten undesirably
                    if (i, j) not in pushed:
                        grid[i][j] = '.'
                        grid[i + dr][j] = char
                        pushed.add((i, j))

            # horizontal pushing
            else:
                self._push_p2_x(grid, row, col, dc, col)

            if grid[row][col] != '@':
                row += dr
                col += dc

        # '[' is always the closest to the left edge of the grid
        return self._gps_sum(grid, '[')

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 1515788
        assert p2 == 1516544