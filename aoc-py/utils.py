
__all__ = (
    'find_start',
    'neighbors_4',
    'neighbors_diag',
)

from typing import Sequence

def find_start(grid: Sequence[Sequence[str]], char: str) -> tuple[int, int]:
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == char:
                return i, j
    raise ValueError(f"No '{char}' character found in grid")

def neighbors_4(row: int, col: int) -> tuple[tuple[int, int], ...]:
    return (
        (row, col - 1),
        (row, col + 1),
        (row - 1, col),
        (row + 1, col),
    )

def neighbors_diag(row: int, col: int) -> tuple[tuple[int, int], ...]:
    return (
        (row - 1, col - 1),
        (row - 1, col + 1),
        (row + 1, col - 1),
        (row + 1, col + 1),
    )