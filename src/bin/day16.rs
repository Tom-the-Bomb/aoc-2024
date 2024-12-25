//! Day 16: Reindeer Maze
//!
//! <https://adventofcode.com/2024/day/16>

use std::{
    collections::{BinaryHeap, HashMap, HashSet},
    fmt::Display,
    cmp::Reverse,
};
use aoc_2024::{Solution, neighbors_4, find_start, get_grid};

pub struct Day16;

impl Day16 {
    fn traverse_maze<T: Display>(inp: T, is_part2: bool) -> usize {
        let grid = get_grid(inp);
        let start @ (start_row, start_col) = find_start(&grid, b'S').unwrap();

        let mut heap = BinaryHeap::new();
        heap.push(Reverse(
            (0, start_row, start_col, 0, 1, Vec::new())
        ));

        let mut scores = HashMap::new();
        let mut all_seats = HashSet::new();
        all_seats.insert(start);

        while let Some(Reverse((score, row, col, dr, dc, seats))) = heap.pop() {
            if grid[row][col] == b'E' {
                if !is_part2 {
                    return score;
                }
                all_seats.extend(seats);
                continue;
            }

            for next_coord @ (next_row, next_col) in neighbors_4(row, col) {
                let next_dr = next_row as isize - row as isize;
                let next_dc = next_col as isize - col as isize;

                if grid[next_row][next_col] == b'#' || next_dr == -dr && next_dc == -dc {
                    continue;
                }

                let next_score = score +
                    if dr == next_dr && dc == next_dc {
                        1
                    } else {
                        1001
                    };

                let key = (next_row, next_col, next_dr, next_dc);

                if *scores.get(&key).unwrap_or(&next_score) >= next_score {
                    scores.insert(key, next_score);

                    let mut seats = seats.clone();
                    seats.push(next_coord);

                    heap.push(Reverse((
                        next_score, next_row, next_col, next_dr, next_dc, seats,
                    )));
                }
            }
        }
        all_seats.len()
    }
}

impl Solution for Day16 {
    const NAME: &'static str = "Reindeer Maze";

    fn part_one<T: Display>(&self, inp: T) -> Self::OutputP1 {
        Self::traverse_maze(inp, false)
    }

    fn part_two<T: Display>(&self, inp: T) -> Self::OutputP2 {
        Self::traverse_maze(inp, true)
    }

    fn run(&self, inp: String) {
        let p1 = self.part_one(&inp);
        let p2 = self.part_two(&inp);

        println!("Part 1: {p1}");
        println!("Part 2: {p2}");

        assert_eq!(p1, 105496);
        assert_eq!(p2, 524);
    }
}

fn main() {
    aoc_2024::run_day(16, &Day16);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}