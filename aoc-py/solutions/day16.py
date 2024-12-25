"""
Day 16: Reindeer Maze

https://adventofcode.com/2024/day/16
"""
__all__ = ('Day16',)

from typing import ClassVar
from heapq import heappop, heappush

from ..solution import Solution
from ..utils import find_start, neighbors_4

class Day16(Solution):
    NAME: ClassVar[str] = 'Reindeer Maze'

    def __init__(self) -> None:
        self.score = None
        self.seats = None

    def _traverse_maze(self, inp: str) -> tuple[int, int]:
        grid = inp.splitlines()
        start = find_start(grid, 'S')

        heap: list[tuple[int, int, int, int, int, tuple[tuple[int, int], ...]]] = []
        heappush(heap, (0, *start, 0, 1, ()))

        scores = {}
        all_seats = {start}

        min_score = 0

        while heap:
            score, row, col, dr, dc, seats = heappop(heap)

            if grid[row][col] == 'E':
                # completed an optimal path to the end
                # union the seats (tiles traversed) in the current path to all of the seats
                all_seats.update(seats)
                # Part 1 answer
                min_score = score
                continue

            for next_row, next_col in neighbors_4(row, col):
                # re-calculate the `dr`` and `dc` to get to the next tile
                next_dr = next_row - row
                next_dc = next_col - col

                # hit a wall or is attempting to go backwards
                if grid[next_row][next_col] == '#' or next_dr == -dr and next_dc == -dc:
                    continue

                # new score: `+1` if straight else `+1001` (`1000` for turning & `1` for moving again in the new direction)
                next_score = score + (
                    1 if next_dr == dr and next_dc == dc else 1001
                )

                # if the next tile has never been traversed with the same direction
                # OR if it has been: the current score is lower and more optimal
                #
                # -> re-traverse
                if scores.get(key := (next_row, next_col, next_dr, next_dc), next_score) >= next_score:
                    scores[key] = next_score
                    heappush(
                        heap,
                        (next_score, *key, seats + ((next_row, next_col),))
                    )

        return min_score, len(all_seats)

    def part_one(self, inp: str) -> int:
        if self.score is None:
            self.score, self.seats = self._traverse_maze(inp)
        return self.score

    def part_two(self, inp: str) -> int:
        if self.seats is None:
            self.score, self.seats = self._traverse_maze(inp)
        return self.seats

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 105496
        assert p2 == 524