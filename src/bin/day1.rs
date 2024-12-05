//! Day 1: Historian Hysteria
//!
//! <https://adventofcode.com/2024/day/1>
use std::{collections::HashMap, fmt::Display};
use aoc_2024::Solution;

pub struct Day1;

impl Solution for Day1 {
    const NAME: &'static str = "Historian Hysteria";

    /// # Panics
    ///
    /// If lines do not follow "<number>   <number>" format
    fn part_one<T: Display>(&self, inp: T) -> usize {
        let mut list1 = Vec::new();
        let mut list2 = Vec::new();

        for line in inp.to_string().lines() {
            let (a, b) = line.split_once("   ").unwrap();

            list1.push(a.parse::<usize>().unwrap());
            list2.push(b.parse::<usize>().unwrap());
        }

        list1.sort_unstable();
        list2.sort_unstable();

        list1.into_iter()
            .zip(list2)
            .map(|(a, b)| a.abs_diff(b))
            .sum()
    }

    fn part_two<T: Display>(&self, inp: T) -> usize {
        let mut list1 = Vec::new();
        let mut counter = HashMap::new();

        for line in inp.to_string().lines() {
            let (a, b) = line.split_once("   ").unwrap();

            list1.push(a.parse::<usize>().unwrap());
            *counter.entry(b.parse::<usize>().unwrap())
                .or_insert(0) += 1;
        }

        list1.sort_unstable();

        list1.into_iter()
            .map(|a| a * counter.get(&a).unwrap_or(&0))
            .sum()
    }

    fn run(&self, inp: String) {
        let p1 = self.part_one(&inp);
        let p2 = self.part_two(&inp);

        println!("Part 1: {p1}");
        println!("Part 2: {p2}");

        assert_eq!(p1, 1_319_616);
        assert_eq!(p2, 27_267_728);
    }
}

fn main() {
    aoc_2024::run_day(1, &Day1);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}