//! Day 10: Hoof It
//!
//! <https://adventofcode.com/2024/day/10>

use std::{
    collections::{VecDeque, HashSet},
    fmt::Display
};
use aoc_2024::{Solution, get_grid, neighbors_4};

pub struct Day10;

impl Solution for Day10 {
    const NAME: &'static str = "Hoof It";

    fn part_one<T: Display>(&self, inp: T) -> usize {
        let grid = get_grid(inp);
        let rows = 0..grid.len();
        let cols = 0..grid[0].len();

        let mut count = 0;

        for (start_i, row) in grid.iter().enumerate() {
            for (start_j, &cell) in row.iter().enumerate() {
                if cell == b'0' {
                    let mut to_check = VecDeque::new();
                    to_check.push_back((start_i, start_j, 0));

                    let mut nines = HashSet::new();

                    while let Some((i, j, num)) = to_check.pop_front() {
                        if num == 9 {
                            nines.insert((i, j));
                        } else {
                            for (next_i, next_j) in neighbors_4(i, j) {
                                if rows.contains(&next_i)
                                    && cols.contains(&next_j)
                                    && grid[next_i][next_j] as usize - 48 == num + 1
                                {
                                    to_check.push_back((next_i, next_j, num + 1));
                                }
                            }
                        }
                    }
                    count += nines.len();
                }
            }
        }
        count
    }

    fn part_two<T: Display>(&self, inp: T) -> usize {
        let grid = get_grid(inp);
        let rows = 0..grid.len();
        let cols = 0..grid[0].len();

        let mut count = 0;

        for (start_i, row) in grid.iter().enumerate() {
            for (start_j, &cell) in row.iter().enumerate() {
                if cell == b'0' {
                    let mut to_check = VecDeque::new();
                    to_check.push_back((start_i, start_j, 0));

                    while let Some((i, j, num)) = to_check.pop_front() {
                        if num == 9 {
                            count += 1;
                        } else {
                            for (next_i, next_j) in neighbors_4(i, j) {
                                if rows.contains(&next_i)
                                    && cols.contains(&next_j)
                                    && grid[next_i][next_j] as usize - 48 == num + 1
                                {
                                    to_check.push_back((next_i, next_j, num + 1));
                                }
                            }
                        }
                    }
                }
            }
        }
        count
    }

    fn run(&self, inp: String) {
        let p1 = self.part_one(&inp);
        let p2 = self.part_two(&inp);

        println!("Part 1: {p1}");
        println!("Part 2: {p2}");

        assert_eq!(p1, 430);
        assert_eq!(p2, 928);
    }
}

fn main() {
    aoc_2024::run_day(10, &Day10);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}