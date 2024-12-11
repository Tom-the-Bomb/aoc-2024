//! Day 11: Plutonian Pebbles
//!
//! <https://adventofcode.com/2024/day/11>

use std::{collections::HashMap, fmt::Display};
use aoc_2024::Solution;

pub struct Day11;

impl Day11 {
    fn blink<T: Display>(inp: T, n: usize) -> usize {
        let mut counter = HashMap::new();

        for stone in inp
            .to_string()
            .split_whitespace()
        {
            *counter.entry(stone.to_string()).or_insert(0) += 1;
        }

        for _ in 0..n {
            let mut new_counter = HashMap::new();

            for (stone, count) in counter {
                if stone == "0" {
                    *new_counter.entry("1".to_string())
                        .or_insert(0) += count;
                } else if stone.len() % 2 == 0 {
                    let (a, b) = stone.split_at(stone.len() / 2);

                    *new_counter.entry(a.to_string())
                        .or_insert(0) += count;
                    *new_counter.entry(
                        match b.trim_start_matches('0') {
                            "" => "0",
                            b => b,
                        }.to_string()
                    )
                        .or_insert(0) += count;
                } else {
                    *new_counter.entry(
                        (stone.parse::<usize>().unwrap() * 2024).to_string()
                    )
                        .or_insert(0) += count;
                }
            }
            counter = new_counter;
        }
        counter.values().sum()
    }
}

impl Solution for Day11 {
    const NAME: &'static str = "Plutonian Pebbles";

    fn part_one<T: Display>(&self, inp: T) -> usize {
        Self::blink(inp, 25)
    }

    fn part_two<T: Display>(&self, inp: T) -> usize {
        Self::blink(inp, 75)
    }

    fn run(&self, inp: String) {
        let p1 = self.part_one(&inp);
        let p2 = self.part_two(&inp);

        println!("Part 1: {p1}");
        println!("Part 2: {p2}");

        assert_eq!(p1, 203_953);
        assert_eq!(p2, 242_090_118_578_155);
    }
}

fn main() {
    aoc_2024::run_day(11, &Day11);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}