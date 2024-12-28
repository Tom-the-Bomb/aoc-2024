//! Day 19: Linen Layout
//!
//! <https://adventofcode.com/2024/day/19>

use std::{collections::HashMap, fmt::Display};
use aoc_2024::Solution;

pub struct Day19;

macro_rules! parse_input {
    ($inp:expr) => {{
        let (options, designs) = $inp
            .split_once("\n\n")
            .unwrap();
        (
            options.split(", ")
                .collect::<Vec<_>>(),
            designs.lines()
                .collect::<Vec<_>>(),
        )
    }}
}

impl Day19 {
    fn create<'a>(design: &'a str, options: &[&str], cache: &mut HashMap<&'a str, usize>) -> usize {
        if let Some(&ways) = cache.get(design) {
            return ways
        }

        if design.is_empty() {
            return 1;
        }

        let ways = options
            .iter()
            .filter(|&&option| design.starts_with(option))
            .map(|&option| Self::create(&design[option.len()..], options, cache))
            .sum();

        cache.insert(design, ways);
        ways
    }
}

impl Solution for Day19 {
    const NAME: &'static str = "Linen Layout";

    fn part_one<T: Display>(&self, inp: T) -> Self::OutputP1 {
        let inp = inp.to_string().replace('\r', "");
        let (options, designs) = parse_input!(inp);
        let mut cache = HashMap::new();

        designs
            .into_iter()
            .filter(|&design| Self::create(design, &options, &mut cache) > 0)
            .count()
    }

    fn part_two<T: Display>(&self, inp: T) -> Self::OutputP2 {
        let inp = inp.to_string().replace('\r', "");
        let (options, designs) = parse_input!(inp);
        let mut cache = HashMap::new();

        designs
            .into_iter()
            .map(|design| Self::create(design, &options, &mut cache))
            .sum()
    }

    fn run(&self, inp: String) {
        let p1 = self.part_one(&inp);
        let p2 = self.part_two(&inp);

        println!("Part 1: {p1}");
        println!("Part 2: {p2}");

        assert_eq!(p1, 311);
        assert_eq!(p2, 616_234_236_468_263);
    }
}

fn main() {
    aoc_2024::run_day(19, &Day19);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}