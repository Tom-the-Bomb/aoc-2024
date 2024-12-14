"""
Day 14: Restroom Redoubt

https://adventofcode.com/2024/day/14
"""
__all__ = ('Day14',)

from typing import ClassVar
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

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 230436441
        assert p2 == 8270