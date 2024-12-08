"""
Day 8: Resonant Collinearity

https://adventofcode.com/2024/day/8
"""
__all__ = ('Day8',)

from typing import ClassVar
from collections import defaultdict
from itertools import combinations

from ..solution import Solution

class Day8(Solution):
    NAME: ClassVar[str] = 'Resonant Collinearity'

    def part_one(self, inp: str) -> int:
        grid = inp.splitlines()
        n_rows = len(grid)
        n_cols = len(grid[0])

        # tracks `frequency` -> [coordinates of antennae with that frequency]
        antennae = defaultdict(set)

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell != '.':
                    antennae[cell].add((i, j))

        antinodes = set()

        for positions in antennae.values():
            # check all pairings of antennae with the same frequency
            for (r1, c1), (r2, c2) in combinations(positions, 2):
                dr = r2 - r1
                dc = c2 - c1

                # potential locations for antinodes at `|<dr, dc>|` away from each antennae in the respective directions
                if (r2 := r2 + dr) in range(n_rows) and (c2 := c2 + dc) in range(n_cols):
                    antinodes.add((r2, c2))
                if (r1 := r1 - dr) in range(n_rows) and (c1 := c1 - dc) in range(n_cols):
                    antinodes.add((r1, c1))
        return len(antinodes)

    def part_two(self, inp: str) -> int:
        grid = inp.splitlines()
        n_rows = len(grid)
        n_cols = len(grid[0])

        antennae = defaultdict(set)
        antinodes = set()

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell != '.':
                    antennae[cell].add((i, j))
                    # antinodes occur on the antennae themselves now too
                    # track them now: more efficient, less redundant additions to set
                    antinodes.add((i, j))

        for positions in antennae.values():
            for (r1, c1), (r2, c2) in combinations(positions, 2):
                dr = r2 - r1
                dc = c2 - c1

                # ONLY difference from part 1: `if` -> `while`
                #
                # antinodes *continuously* occur along the line at these intervals
                while (r2 := r2 + dr) in range(n_rows) and (c2 := c2 + dc) in range(n_cols):
                    antinodes.add((r2, c2))
                while (r1 := r1 - dr) in range(n_rows) and (c1 := c1 - dc) in range(n_cols):
                    antinodes.add((r1, c1))

        return len(antinodes)

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 367
        assert p2 == 1285