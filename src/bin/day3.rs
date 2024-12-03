//! Day 3: Mull It Over
//!
//! <https://adventofcode.com/2024/day/3>

use std::fmt::Display;
use regex::Regex;
use aoc_2024::Solution;

pub struct Day3;

impl Solution for Day3 {
    const NAME: &'static str = "Mull It Over";

    fn part_one<T: Display>(&self, inp: T) -> usize {
        Regex::new(r"mul\(([0-9]+),([0-9]+)\)")
            .unwrap()
            .captures_iter(&*inp.to_string())
            .map(|c| {
                let (_, [a, b]) = c.extract();

                a.parse::<usize>().unwrap() * b.parse::<usize>().unwrap()
            })
            .sum()
    }

    fn part_two<T: Display>(&self, inp: T) -> usize {
        let mut add = true;
        let mut total = 0;

        for c in Regex::new(r"mul\(([0-9]+),([0-9]+)\)|do\(()()\)|don\'t\(()()\)")
            .unwrap()
            .captures_iter(&*inp.to_string())
        {
            match c.extract() {
                ("do()", _) => add = true,
                ("don't()", _) => add = false,
                (_, [a, b]) => if add {
                    total += a.parse::<usize>().unwrap() * b.parse::<usize>().unwrap();
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

        assert_eq!(p1, 164730528);
        assert_eq!(p2, 70478672);
    }
}

fn main() {
    aoc_2024::run_day(3, &Day3);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}