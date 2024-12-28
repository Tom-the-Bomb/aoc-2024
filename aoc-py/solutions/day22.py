"""
Day 22: Monkey Market

https://adventofcode.com/2024/day/22
"""
__all__ = ('Day22',)

from typing import ClassVar
from collections import defaultdict

from ..solution import Solution

class Day22(Solution):
    NAME: ClassVar[str] = 'Monkey Market'

    def _calc_next_secret(self, secret: int) -> int:
        secret ^= secret * 64
        secret %= 16777216
        secret ^= secret // 32
        secret ^= secret * 2048
        secret %= 16777216
        return secret

    def part_one(self, inp: str) -> int:
        total = 0

        for secret in inp.splitlines():
            secret = int(secret)

            for _ in range(2000):
                secret = self._calc_next_secret(secret)

            total += secret
        return total

    def part_two(self, inp: str) -> int:
        bananas = defaultdict(int)

        # for each buyer:
        for secret in inp.splitlines():
            secret = int(secret)

            # initial price = initial seccret value (last digit)
            prices = [int(str(secret)[-1])]
            # store the price deltas as `differences[i] = prices[i + 1] - prices[i]`
            differences = []

            seen = set()

            for _ in range(2000):
                secret = self._calc_next_secret(secret)

                # next price (last digit of next secret valye)
                price = int(str(secret)[-1])

                # record the price delta (change since previous price)
                differences.append(price - prices[-1])
                # record new price
                prices.append(price)

                # try the most recent 4 price deltas as our "sequence"
                sequence = tuple(differences[-4:])

                # make sure it's not too short (occurs at the beginning when there aren't enough prices)
                #
                # make sure we don't record sequences that have already occured before i the buyer's secret history
                # this is because the monkey will sell at the first instance
                if len(sequence) == 4 and sequence not in seen:
                    seen.add(sequence)

                    # record the total number of bananas obtained using the current `sequence` from all buyers
                    bananas[sequence] += price

        # return max bananas obtained from any sequence
        return max(bananas.values())

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 13022553808
        assert p2 == 1555