"""
Day 24: Crossed Wires

https://adventofcode.com/2024/day/24
"""
__all__ = ('Day24',)

from typing import ClassVar
from collections import deque

from ..solution import Solution

class Day24(Solution):
    NAME: ClassVar[str] = 'Crossed Wires'

    def part_one(self, inp: str) -> int:
        initial, operations = inp.split('\n\n')

        wires: dict[str, int] = {}
        for wire in initial.splitlines():
            wire, val = wire.split(':')
            wires[wire] = int(val)

        # evaluate operations in a queue-like fashion as not all operations can be evaluated immediately
        # and must wait until their operands exist after evaluating other operations first
        operations = deque(
            operation.split() for operation in operations.splitlines()
        )

        while operations:
            left, op, right, _, out = operation = operations.popleft()

            # operation is able to be evaluated
            # store result into `out` wire (helping open up more operations that can be evaluated)
            if (left := wires.get(left)) is not None and (right := wires.get(right)) is not None:
                match op:
                    case 'AND':
                        wires[out] = left & right
                    case 'OR':
                        wires[out] = left | right
                    case 'XOR':
                        wires[out] = left ^ right
            else:
                # required operands don't exist yet: push to end of queue to try again later
                operations.append(operation)

        # sort z-wires by index
        z_wires = sorted([
            (wire, val) for wire, val in wires.items() if wire.startswith('z')
        ])

        # convert sorted z-wire values from binary to decimal
        return sum(
            val * 2 ** exp
            for exp, (_, val) in enumerate(z_wires)
        )

    def part_two(self, inp: str) -> int:
        ...

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 55730288838374
        #assert p2 == 70478672