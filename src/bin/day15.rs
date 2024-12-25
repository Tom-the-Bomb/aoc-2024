//! Day 15: Warehouse Woes
//!
//! <https://adventofcode.com/2024/day/15>

use std::fmt::Display;
use aoc_2024::Solution;

pub struct Day15;

impl Solution for Day15 {
    const NAME: &'static str = "Warehouse Woes";

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

        assert_eq!(p1, 164_7150_528);
        assert_eq!(p2, 70_478_672);
    }
}

fn main() {
    aoc_2024::run_day(15, &Day15);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}