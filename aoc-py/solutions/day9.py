"""
Day 9: Disk Fragmenter

https://adventofcode.com/2024/day/9
"""
__all__ = ('Day9',)

from typing import ClassVar

from ..solution import Solution

class Day9(Solution):
    NAME: ClassVar[str] = 'Disk Fragmenter'

    def part_one(self, inp: str) -> int:
        disk = []
        num = 0

        for i, count in enumerate(inp):
            count = int(count)
            if i % 2 == 0:
                disk += [num] * count
                num += 1
            else:
                disk += [None] * count

        i = 0
        while i < len(disk):
            if disk[i] is None:
                if (last := disk.pop()) is None:
                    # simply try again as this continues the loop without increasing `i`
                    continue

                disk[i] = last
            i += 1

        return sum(
            i * num for i, num in enumerate(disk)
        )

    def part_two(self, inp: str) -> int:
        # the parsed disk: '123' -> '0..111'
        disk = []
        # stores a list of the indices interval `[start, stop)` in which each contiguous block of space occupies in the disk
        #
        # i.e. the '..' in '0..111' would be stored as `slice(1, 3)`
        spaces: list[slice] = []
        # stores a list of the literal block and the indices interval `[start, stop)` in which it occupies in the disk
        #
        # i.e. the '111' in '0..111' would be stored as `([1, 1, 1], slice(3, 6))`
        blocks: list[tuple[list[int], slice]] = []

        num = 0

        for i, count in enumerate(inp):
            count = int(count)
            # the start index of the next block will be the length of the existing disk
            start = len(disk)
            interval = slice(start, start + count)

            if i % 2 == 0:
                blocks.append((
                    block := [num] * count,
                    interval,
                ))
                disk += block
                num += 1
            else:
                spaces.append(interval)
                disk += [None] * count

        # try and find a space for all the blocks starting at the end
        for block, block_slice in reversed(blocks):
            block_size = block_slice.stop - block_slice.start

            for i, space in enumerate(spaces):
                space_size = space.stop - space.start

                # found an empty `space` *big enough* and *occurs before* for our `block` to move itself into
                if block_size <= space_size and space.start < block_slice.start:

                    if block_size == space_size:
                        # OPTIMIZATION: remove completely occupied blocks from list
                        del spaces[i]
                    else:
                        # cut off the start of the space that is now occupied by the block
                        spaces[i] = slice(space.start + block_size, space.stop)

                    # replace block's original spot with '...'
                    disk[block_slice] = [None] * block_size
                    # replace the `block_size` sized portion at the start of the `space` with the block itself
                    disk[space.start:space.start + block_size] = block

                    break

        return sum(
            i * num for i, num in enumerate(disk) if num is not None
        )

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 6356833654075
        assert p2 == 6389911791746