//! Day 4: Ceres Search
//!
//! <https://adventofcode.com/2024/day/4>

use std::{collections::HashSet, fmt::Display};
use aoc_2024::Solution;

pub struct Day4;

static DIRECTIONS: [(i8, i8); 8] = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
];
static XMAS: &[u8; 4] = b"XMAS";

lazy_static::lazy_static! {
    static ref CORNERS: HashSet<u8> = HashSet::from_iter([b'M', b'S']);
}

impl Day4 {
    #[inline]
    #[must_use]
    fn get_grid<T: Display>(inp: T) -> Vec<Vec<u8>> {
        inp.to_string()
            .lines()
            .map(|line| line.as_bytes().to_vec())
            .collect::<Vec<_>>()
    }

    #[must_use]
    fn find_xmas(
        grid: &[Vec<u8>],
        n_rows: usize,
        n_cols: usize,
        i: usize, j: usize,
        dr: usize, dc: usize,
        progression: usize,
    ) -> bool {
        if progression == 4 {
            return true;
        }

        if !(0..n_rows).contains(&i) || !(0..n_cols).contains(&j) {
            return false;
        }

        if grid[i][j] == XMAS[progression] {
            return Self::find_xmas(
                grid,
                n_rows, n_cols,
                i.wrapping_add(dr),
                j.wrapping_add(dc),
                dr, dc,
                progression + 1,
            )
        }
        false
    }
}

impl Solution for Day4 {
    const NAME: &'static str = "Ceres Search";

    fn part_one<T: Display>(&self, inp: T) -> usize {
        let grid = &Self::get_grid(inp);
        let n_rows = grid.len();
        let n_cols = grid[0].len();

        (0..n_rows)
            .flat_map(|i| (0..n_cols)
                .flat_map(move |j| DIRECTIONS
                    .iter()
                    .filter(move |&&(dr, dc)| Self::find_xmas(grid, n_rows, n_cols, i, j, dr as usize, dc as usize, 0))
                )
            )
            .count()
    }

    fn part_two<T: Display>(&self, inp: T) -> usize {
        let grid = &Self::get_grid(inp);
        let n_cols = grid[0].len();

        (1..grid.len() - 1)
            .flat_map(|i| (1..n_cols - 1)
                .filter(move |&j| {
                    if grid[i][j] != b'A' {
                        return false;
                    }

                    let diag1 = HashSet::from_iter([
                        grid[i - 1][j - 1],  grid[i + 1][j + 1]
                    ]);
                    let diag2 = HashSet::from_iter([
                        grid[i - 1][j + 1],  grid[i + 1][j - 1]
                    ]);
                    diag1 == *CORNERS && diag2 == *CORNERS
                })
            )
            .count()
    }

    fn run(&self, inp: String) {
        let p1 = self.part_one(&inp);
        let p2 = self.part_two(&inp);

        println!("Part 1: {p1}");
        println!("Part 2: {p2}");

        assert_eq!(p1, 2578);
        assert_eq!(p2, 1972);
    }
}

fn main() {
    aoc_2024::run_day(4, &Day4);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}