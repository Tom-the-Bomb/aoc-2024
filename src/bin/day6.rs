//! Day 6: Guard Gallivant
//!
//! <https://adventofcode.com/2024/day/6>

use std::{
    collections::HashSet,
    fmt::Display,
    ops::Range,
};
use aoc_2024::{Solution, get_grid, find_start};

pub struct Day6;

impl Day6 {
    fn turn_right(dr: i8, dc: i8) -> (i8, i8) {
        match (dr, dc) {
            (1, 0) => (0, -1),
            (-1, 0) => (0, 1),
            (0, 1) => (1, 0),
            (0, -1) => (-1, 0),
            _ => unreachable!(),
        }
    }

    #[allow(clippy::cast_sign_loss)]
    fn get_path(
        grid: &[Vec<u8>],
        rows: &Range<usize>,
        cols: &Range<usize>,
        start @ (mut row, mut col): (usize, usize),
    ) -> HashSet<(usize, usize)> {
        let mut dr = -1;
        let mut dc = 0;

        let mut seen = HashSet::new();
        seen.insert(start);

        loop {
            row = row.wrapping_add(dr as usize);
            col = col.wrapping_add(dc as usize);

            if !rows.contains(&row) || !cols.contains(&col) {
                break seen;
            }

            if grid[row][col] == b'#' {
                row = row.wrapping_sub(dr as usize);
                col = col.wrapping_sub(dc as usize);

                (dr, dc) = Self::turn_right(dr, dc);
            } else {
                seen.insert((row, col));
            }
        }
    }
}

impl Solution for Day6 {
    const NAME: &'static str = "Guard Gallivant";

    fn part_one<T: Display>(&self, inp: T) -> Self::OutputP1 {
        let grid = get_grid(inp);
        let start = find_start(&grid, b'^').unwrap();

        let rows = 0..grid.len();
        let cols = 0..grid[0].len();

        Self::get_path(&grid, &rows, &cols, start).len()
    }

    #[allow(clippy::cast_sign_loss)]
    fn part_two<T: Display>(&self, inp: T) -> Self::OutputP2 {
        let grid = get_grid(inp);
        let start = find_start(&grid, b'^').unwrap();

        let rows = 0..grid.len();
        let cols = 0..grid[0].len();

        let mut total = 0;

        for obstacle in Self::get_path(&grid, &rows, &cols, start) {
            let (mut row, mut col) = start;

            let mut dr = -1;
            let mut dc = 0;

            let mut seen = HashSet::new();
            seen.insert((row, col, dr, dc));

            loop {
                row = row.wrapping_add(dr as usize);
                col = col.wrapping_add(dc as usize);

                if seen.contains(&(row, col, dr, dc)) {
                    total += 1;
                    break;
                }

                if !rows.contains(&row) || !cols.contains(&col) {
                    break;
                }

                if grid[row][col] == b'#' || (row, col) == obstacle {
                    row = row.wrapping_sub(dr as usize);
                    col = col.wrapping_sub(dc as usize);

                    (dr, dc) = Self::turn_right(dr, dc);
                } else {
                    seen.insert((row, col, dr, dc));
                }
            }
        }
        total
    }

    fn run(&self, inp: String) {
        let p1 = self.part_one(&inp);
        let p2 = self.part_two(&inp);

        println!("Part 1: {p1}");
        println!("Part 2: {p2}");

        assert_eq!(p1, 4696);
        assert_eq!(p2, 1443);
    }
}

fn main() {
    aoc_2024::run_day(6, &Day6);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}