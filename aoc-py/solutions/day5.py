"""
Day 5: Print Queue

https://adventofcode.com/2024/day/5
"""
__all__ = ('Day5',)

from typing import ClassVar
from collections import defaultdict

from ..solution import Solution

class Day5(Solution):
    NAME: ClassVar[str] = 'Print Queue'

    def part_one(self, inp: str) -> int:
        rules, updates = inp.split('\n\n', maxsplit=1)
        rules = [rule.split('|', maxsplit=1) for rule in rules.splitlines()]
        updates = [update.split(',') for update in updates.splitlines()]

        total = 0

        for update in updates:
            # keeps track of the location of all the pages
            indices = {}

            for i, page in enumerate(update):
                indices[page] = i

            for a, b in rules:
                # checks if the current rule `a|b` is relevant (pages exist in update)
                #
                # and if `a` exists at `i` and `b` exists at `j`:
                # and `i > j` => the page is henceforth invalid
                if (i := indices.get(a)) is not None and (j := indices.get(b)) is not None and i > j:
                    break
            else:
                # no break => valid
                total += int(update[len(update) // 2])

        return total

    def part_two(self, inp: str) -> int:
        rules, updates = inp.split('\n\n', maxsplit=1)
        rules = [rule.split('|', maxsplit=1) for rule in rules.splitlines()]
        updates = [update.split(',') for update in updates.splitlines()]

        total = 0

        for update in updates:
            indices = {}

            for i, page in enumerate(update):
                indices[page] = i

            # maps K -> (# of times the rule `K|<any>` occurs in the ruleset)
            counter = defaultdict(int)
            invalid = False

            for a, b in rules:
                if (i := indices.get(a)) is not None and (j := indices.get(b)) is not None:
                    # only count rules with pages that exist in the current update
                    # otherwise it will mess up the sorting as we will have overcounted
                    counter[a] += 1

                    if i > j:
                        invalid = True

            if invalid:
                # sorts the update to make it valid
                #
                # pages with more pages that are supposed to be after it: (high `counter[page]` value) should go at the start and vice versa
                update.sort(key=lambda page: -counter[page])
                total += int(update[len(update) // 2])
        return total

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 4872
        assert p2 == 5564