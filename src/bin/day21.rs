//! Day 17: Chronospatial Computer
//!
//! <https://adventofcode.com/2024/day/17>

use std::fmt::Display;
use aoc_2024::Solution;

pub struct Day17;

impl Solution for Day17 {
    const NAME: &'static str = "Chronospatial Computer";

    fn part_one<T: Display>(&self, _inp: T) -> Self::OutputP1 {
        todo!()
    }

    fn part_two<T: Display>(&self, _inp: T) -> Self::OutputP2 {
        todo!()
    }

    fn run(&self, inp: String) {
        let p1 = self.part_one(&inp);
        let p2 = self.part_two(&inp);

        println!("Part 1: {p1}");
        println!("Part 2: {p2}");

        assert_eq!(p1, 1_647_170_528);
        assert_eq!(p2, 70_478_672);
    }
}

fn main() {
    aoc_2024::run_day(17, &Day17);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}