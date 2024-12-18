"""
Day 18: RAM Run

https://adventofcode.com/2024/day/18
"""
__all__ = ('Day18',)

from typing import ClassVar
from collections import deque

from ..solution import Solution
from ..utils import neighbors_4

class Day18(Solution):
    NAME: ClassVar[str] = 'RAM Run'

    def _parse_corrupted(self, inp: str) -> list[tuple[int, ...]]:
        return [
            tuple(int(x) for x in line.split(','))
            for line in inp.splitlines()
        ]

    def _find_path(self, corrupted: list[tuple[int, ...]], bytes_fell: int) -> int | None:
        n_rows = 71
        n_cols = 71

        corrupted_set = set(corrupted[:bytes_fell])

        to_check = deque([(0, 0, 0)])
        seen = {(0, 0)}

        while to_check:
            row, col, steps = to_check.popleft()

            if row == n_rows - 1 and col == n_cols - 1:
                return steps

            for next_coord in neighbors_4(row, col):
                next_row, next_col = next_coord

                if (
                    next_row in range(n_rows)
                    and next_col in range(n_cols)
                    and next_coord not in corrupted_set
                    and next_coord not in seen
                ):
                    to_check.append((*next_coord, steps + 1))
                    seen.add(next_coord)

    def part_one(self, inp: str) -> int:
        corrupted = self._parse_corrupted(inp)

        assert (steps := self._find_path(corrupted, 1024)) is not None
        return steps

    def part_two(self, inp: str) -> str:
        corrupted = self._parse_corrupted(inp)

        # Lower bound: Part 1 guarantees that the first 1024 bytes will not block the exit
        left = 1024
        # Upper bound: all bytes fell
        right = len(corrupted) - 1

        # binary search only having `mid` number of blocks fall
        #
        # As more bytes fall sequentially -> more likely the path is to be blocked (hence our searching medium is "sorted")
        while left <= right:
            mid = (left + right) // 2

            if self._find_path(corrupted, mid) is None:
                # we blocked the exit! Try even less corrupted bytes and see if the exit is still blocked
                # (optimize as we need to find the first byte that does this)
                right = mid - 1
            else:
                # exit still reachable: Try having more corrupted bytes fall in
                left = mid + 1

        # The first byte that when fell, will block the exit
        byte = corrupted[mid]
        return '{},{}'.format(*byte)

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 302
        assert p2 == '24,32'