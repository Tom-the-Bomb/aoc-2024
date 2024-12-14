//! Day 12: Garden Groups
//!
//! <https://adventofcode.com/2024/day/12>

use std::{
    collections::{HashSet, VecDeque},
    fmt::Display
};
use aoc_2024::{
    Solution,
    get_grid,
    neighbors_4,
    neighbors_diag,
};

pub struct Day12;

impl Solution for Day12 {
    const NAME: &'static str = "Garden Groups";

    fn part_one<T: Display>(&self, inp: T) -> usize {
        let grid = get_grid(inp);
        let rows = 0..grid.len();
        let cols = 0..grid[0].len();

        let mut seen = HashSet::new();
        let mut total = 0;

        for (start_i, row) in grid.iter().enumerate() {
            for (start_j, &cell) in row.iter().enumerate() {
                let start = (start_i, start_j);

                if !seen.contains(&start) {
                    let mut to_check = VecDeque::new();
                    to_check.push_back(start);

                    let mut local_seen = HashSet::new();
                    local_seen.insert(start);

                    let mut perimeter = 0;

                    while let Some((i, j)) = to_check.pop_front() {
                        perimeter += 4;

                        for next @ (next_i, next_j) in neighbors_4(i, j) {
                            if rows.contains(&next_i)
                                && cols.contains(&next_j)
                                && grid[next_i][next_j] == cell
                            {
                                if !local_seen.contains(&next) {
                                    to_check.push_back(next);
                                    local_seen.insert(next);
                                }
                                perimeter -= 1;
                            }
                        }
                    }
                    total += perimeter * local_seen.len();
                    seen.extend(local_seen);
                }
            }
        }
        total
    }

    fn part_two<T: Display>(&self, inp: T) -> usize {
        let grid = get_grid(inp);
        let rows = 0..grid.len();
        let cols = 0..grid[0].len();

        let mut seen = HashSet::new();
        let mut total = 0;

        for (start_i, row) in grid.iter().enumerate() {
            for (start_j, &cell) in row.iter().enumerate() {
                let start = (start_i, start_j);

                if !seen.contains(&start) {
                    let mut to_check = VecDeque::new();
                    to_check.push_back(start);

                    let mut local_seen = HashSet::new();
                    local_seen.insert(start);

                    let mut corners = 0;

                    while let Some((i, j)) = to_check.pop_front() {

                        for next @ (next_i, next_j) in neighbors_4(i, j) {
                            if rows.contains(&next_i)
                                && cols.contains(&next_j)
                                && grid[next_i][next_j] == cell
                                && !local_seen.contains(&next)
                            {
                                to_check.push_back(next);
                                local_seen.insert(next);
                            }
                        }

                        for (adj_i, adj_j) in neighbors_diag(i, j) {
                            let side1_exists = rows.contains(&adj_i);
                            let side2_exists = rows.contains(&adj_j);

                            if (
                                (!side1_exists || grid[adj_i][j] != cell)
                                && (!side2_exists || grid[i][adj_j] != cell)
                            ) || (
                                side1_exists
                                && side2_exists
                                && grid[adj_i][j] == cell
                                && grid[i][adj_j] == cell
                                && grid[adj_i][adj_j] != cell
                            ) {
                                corners += 1;
                            }
                        }
                    }
                    total += corners * local_seen.len();
                    seen.extend(local_seen);
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

        assert_eq!(p1, 1_375_574);
        assert_eq!(p2, 830_566);
    }
}

fn main() {
    aoc_2024::run_day(12, &Day12);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}