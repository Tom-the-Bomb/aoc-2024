//! Day 18: RAM Run
//!
//! <https://adventofcode.com/2024/day/18>

use std::{
    collections::{HashSet, VecDeque},
    fmt::Display
};
use aoc_2024::{Solution, neighbors_4};

pub struct Day18;

impl Day18 {
    fn parse_corrupted<T: Display>(inp: T) -> Vec<(usize, usize)> {
        inp
            .to_string()
            .lines()
            .map(|line| {
                let (x, y) = line.split_once(',').unwrap();
                (
                    x.parse::<usize>().unwrap(),
                    y.parse::<usize>().unwrap(),
                )
            })
            .collect()
    }

    fn find_path(corrupted: &Vec<(usize, usize)>, bytes_fell: usize) -> Option<usize> {
        let rows = 0..=70;
        let cols = 0..=70;

        let corrupted_set = HashSet::<&(usize, usize)>::from_iter(&corrupted[..bytes_fell]);

        let mut to_check = VecDeque::new();
        to_check.push_back((0, 0, 0));

        let mut seen = HashSet::new();
        seen.insert((0, 0));

        while let Some((row, col, steps)) = to_check.pop_front() {
            if row == *rows.end() && col == *cols.end() {
                return Some(steps);
            }

            for next_coord @ (next_row, next_col) in neighbors_4(row, col) {
                if rows.contains(&next_row)
                    && cols.contains(&next_col)
                    && !corrupted_set.contains(&next_coord)
                    && seen.insert(next_coord)
                {
                    to_check.push_back((next_row, next_col, steps + 1));
                }
            }
        }
        None
    }
}

impl Solution for Day18 {
    const NAME: &'static str = "RAM Run";

    type OutputP2 = String;

    fn part_one<T: Display>(&self, inp: T) -> Self::OutputP1 {
        Self::find_path(
            &Self::parse_corrupted(inp),
            1024,
        )
        .unwrap()
    }

    fn part_two<T: Display>(&self, inp: T) -> Self::OutputP2 {
        let corrupted = Self::parse_corrupted(inp);

        let mut left = 1024;
        let mut right = corrupted.len() - 1;
        let mut mid = 0;

        while left <= right {
            mid = (left + right) / 2;

            if Self::find_path(&corrupted, mid).is_none() {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        let byte = corrupted[mid];
        return format!("{},{}", byte.0, byte.1);
    }

    fn run(&self, inp: String) {
        let p1 = self.part_one(&inp);
        let p2 = self.part_two(&inp);

        println!("Part 1: {p1}");
        println!("Part 2: {p2}");

        assert_eq!(p1, 302);
        assert_eq!(p2, "24,32");
    }
}

fn main() {
    aoc_2024::run_day(18, &Day18);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}