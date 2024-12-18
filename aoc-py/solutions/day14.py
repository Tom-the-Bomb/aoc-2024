"""
Day 14: Restroom Redoubt

https://adventofcode.com/2024/day/14
"""
__all__ = ('Day14',)

from typing import ClassVar
from zlib import compress
import re

from ..solution import Solution

class Day14(Solution):
    NAME: ClassVar[str] = 'Restroom Redoubt'

    def _get_robots(self, inp: str) -> list[list[int]]:
        return [
            [int(val) for val in robot]
            for robot in re.findall(
                r'p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)',
                inp,
            )
        ]

    def part_one(self, inp: str) -> int:
        robots = self._get_robots(inp)
        w = 101
        h = 103

        hw = w // 2
        hh = h // 2

        q1 = q2 = q3 = q4 = 0

        for x, y, vx, vy in robots:
            # 100 seconds later:
            x += 100 * vx
            y += 100 * vy
            x %= w
            y %= h

            if y < hh:
                if x < hw:
                    q1 += 1
                elif x > hw:
                    q2 += 1
            elif y > hh:
                if x < hw:
                    q3 += 1
                elif x > hw:
                    q4 += 1

        return q1 * q2 * q3 * q4

    def part_two(self, inp: str) -> int:
        robots = self._get_robots(inp)
        w = 101
        h = 103

        t = 0
        while True:
            positions = [
                ((x + t * vx) % w, (y + t * vy) % h)
                for x, y, vx, vy, in robots
            ]
            # Find tree by finding frame where all robots are at unique positions
            if len(set(positions)) == len(positions):
                return t
            t += 1

    def part_two_entropy(self, inp: str) -> int:
        robots = self._get_robots(inp)
        w = 101
        h = 103

        min_entropy = float('inf')
        time = 0

        for t in range(1, 10000):
            positions = {
                ((x + t * vx) % w, (y + t * vy) % h)
                for x, y, vx, vy, in robots
            }

            # use size of zlib compression as a measure of entropy
            #
            # when there is a tree => there is a cluster => low entropy
            # (inefficient and slow)
            if (entropy := len(compress(
                '\n'.join(
                    ''.join('O' if (i, j) in positions else '.' for j in range(w))
                    for i in range(h)
                ).encode()
            ))) < min_entropy:
                min_entropy = entropy
                time = t
        return time

    def part_two_p1_entropy(self, inp: str) -> int:
        robots = self._get_robots(inp)
        w = 101
        h = 103

        hw = w // 2
        hh = h // 2

        min_part_one = float('inf')
        time = 0

        for t in range(1, 10000):
            q1 = q2 = q3 = q4 = 0

            # Use the answer from part 1 as a measure of relative entropy value
            #
            # (more efficient yet sufficient entropy algorithm)
            for x, y, vx, vy in robots:
                x += t * vx
                y += t * vy
                x %= w
                y %= h

                if y < hh:
                    if x < hw:
                        q1 += 1
                    elif x > hw:
                        q2 += 1
                elif y > hh:
                    if x < hw:
                        q3 += 1
                    elif x > hw:
                        q4 += 1

            if (part_one := q1 * q2 * q3 * q4) < min_part_one:
                min_part_one = part_one
                time = t
        return time

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 230436441
        assert p2 == 8270