"""
Day 11: Plutonian Pebbles

https://adventofcode.com/2024/day/11
"""
__all__ = ('Day11',)

from typing import ClassVar
from collections import Counter

from ..solution import Solution

class Day11(Solution):
    NAME: ClassVar[str] = 'Plutonian Pebbles'

    def _blink(self, inp: str, n: int) -> int:
        # major optimization:
        #
        # - repetitive stones with the same value wll be generated quite often: store their frequencies as they weill behave the same
        # - reduces memory used when storing stones and processing time
        #
        # - order of stones does not matter
        counter = Counter(inp.split())

        for _ in range(n):
            new_counter = Counter()

            for stone, count in counter.items():
                if stone == '0':
                    new_counter['1'] += count
                elif (n := len(stone)) % 2 == 0:
                    half = n // 2
                    a, b = stone[:half], stone[half:]

                    new_counter[a] += count
                    new_counter[b.lstrip('0') or '0'] += count
                else:
                    new_counter[str(int(stone) * 2024)] += count

            counter = new_counter
        return sum(counter.values())

    def part_one(self, inp: str) -> int:
        return self._blink(inp, 25)

    def part_two(self, inp: str) -> int:
        return self._blink(inp, 75)

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 203953
        assert p2 == 242090118578155