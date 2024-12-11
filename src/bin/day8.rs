//! Day 8: Resonant Collinearity
//!
//! <https://adventofcode.com/2024/day/8>

use std::{
    collections::{HashSet, HashMap},
    fmt::Display
};
use aoc_2024::{Solution, get_grid};
use itertools::Itertools;

pub struct Day8;

impl Solution for Day8 {
    const NAME: &'static str = "Resonant Collinearity";

    fn part_one<T: Display>(&self, inp: T) -> usize {
        let grid = get_grid(inp);
        let rows = 0..grid.len();
        let cols = 0..grid[0].len();

        let mut antennae = HashMap::new();

        for (i, row) in grid.iter().enumerate() {
            for (j, cell) in row.iter().enumerate() {
                if cell != &b'.' {
                    antennae.entry(cell)
                        .or_insert_with(Vec::new)
                        .push((i, j));
                }
            }
        }

        let mut antinodes = HashSet::new();

        for positions in antennae.into_values() {
            for ((mut r1, mut c1), (mut r2, mut c2)) in positions
                .into_iter()
                .tuple_combinations()
            {
                let dr = r2.wrapping_sub(r1);
                let dc = c2.wrapping_sub(c1);

                r2 = r2.wrapping_add(dr);
                c2 = c2.wrapping_add(dc);
                r1 = r1.wrapping_sub(dr);
                c1 = c1.wrapping_sub(dc);

                if rows.contains(&r2) && cols.contains(&c2) {
                    antinodes.insert((r2, c2));
                }

                if rows.contains(&r1) && cols.contains(&c1) {
                    antinodes.insert((r1, c1));
                }
            }
        }
        antinodes.len()
    }

    fn part_two<T: Display>(&self, inp: T) -> usize {
        let grid = get_grid(inp);
        let rows = 0..grid.len();
        let cols = 0..grid[0].len();

        let mut antennae = HashMap::new();
        let mut antinodes = HashSet::new();

        for (i, row) in grid.iter().enumerate() {
            for (j, cell) in row.iter().enumerate() {
                if cell != &b'.' {
                    antinodes.insert((i, j));
                    antennae.entry(cell)
                        .or_insert_with(Vec::new)
                        .push((i, j));
                }
            }
        }

        for positions in antennae.into_values() {
            for ((mut r1, mut c1), (mut r2, mut c2)) in positions
                .into_iter()
                .tuple_combinations()
            {
                let dr = r2.wrapping_sub(r1);
                let dc = c2.wrapping_sub(c1);

                r2 = r2.wrapping_add(dr);
                c2 = c2.wrapping_add(dc);
                r1 = r1.wrapping_sub(dr);
                c1 = c1.wrapping_sub(dc);

                while rows.contains(&r2) && cols.contains(&c2) {
                    antinodes.insert((r2, c2));

                    r2 = r2.wrapping_add(dr);
                    c2 = c2.wrapping_add(dc);
                }

                while rows.contains(&r1) && cols.contains(&c1) {
                    antinodes.insert((r1, c1));

                    r1 = r1.wrapping_sub(dr);
                    c1 = c1.wrapping_sub(dc);
                }
            }
        }
        antinodes.len()
    }

    fn run(&self, inp: String) {
        let p1 = self.part_one(&inp);
        let p2 = self.part_two(&inp);

        println!("Part 1: {p1}");
        println!("Part 2: {p2}");

        assert_eq!(p1, 367);
        assert_eq!(p2, 1285);
    }
}

fn main() {
    aoc_2024::run_day(8, &Day8);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}