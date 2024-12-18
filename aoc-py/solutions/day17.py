"""
Day 17: Chronospatial Computer

https://adventofcode.com/2024/day/17
"""
__all__ = ('Day17',)

from typing import ClassVar
import re

from ..solution import Solution

class Day17(Solution):
    NAME: ClassVar[str] = 'Chronospatial Computer'

    def _combo(self, operand: int, a: int, b: int, c: int) -> int:
        return (
            operand if operand <= 3
            else a if operand == 4
            else b if operand == 5
            else c if operand == 6
            else 0
        )

    def part_one(self, inp: str) -> str:
        a, b, c, *program = map(int, re.findall(r'([0-9]+)', inp))

        output = []
        pointer = 0

        while pointer < len(program) - 1:
            opcode = program[pointer]
            operand = program[pointer + 1]

            pointer += 2

            match opcode:
                case 0:
                    # note: `p / 2^q` is the same as `p >> q`
                    a >>= self._combo(operand, a, b, c)
                case 1:
                    b ^= operand
                case 2:
                    b = self._combo(operand, a, b, c) % 8
                case 3:
                    if a != 0:
                        pointer = operand
                case 4:
                    b ^= c
                case 5:
                    output.append(self._combo(operand, a, b, c) % 8)
                case 6:
                    b = a >> self._combo(operand, a, b, c)
                case 7:
                    c = a >> self._combo(operand, a, b, c)

        return ','.join(map(str, output))

    def _find_a(self, program: list[int], ans: int) -> int:
        """
        [Instructions]:
        2,4
        1,5
        7,5
        1,6
        4,2
        5,5
        0,3
        3,0

        [Program]:
        b = a % 8
        b = b ^ 5
        c = a >> b
        b = b ^ 6
        b = b ^ c
        out b % 8
        a = a >> 3
        if a == 0 jump 0
        """
        if not program:
            return ans

        b = 0
        c = 0

        for t in range(8):
            a = ans << 3 | t
            b = a % 8
            b ^= 5
            c = a >> b
            b ^= 6
            b ^= c

            if b % 8 == program[-1]:
                if (sub := self._find_a(program[:-1], a)) == -1:
                    continue
                return sub
        return -1

    def part_two(self, inp: str) -> int:
        _, _, _, *program = map(int, re.findall(r'([0-9]+)', inp))

        return self._find_a(program, 0)

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == '2,7,6,5,6,0,2,3,1'
        assert p2 == 107416870455451