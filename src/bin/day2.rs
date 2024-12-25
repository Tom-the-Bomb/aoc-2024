//! Day 2: Red-Nosed Reports
//!
//! <https://adventofcode.com/2024/day/2>
#![feature(array_windows)]

use std::fmt::Display;
use aoc_2024::Solution;

pub struct Day2;

impl Solution for Day2 {
    const NAME: &'static str = "Red-Nosed Reports";

    fn part_one<T: Display>(&self, inp: T) -> Self::OutputP1 {
        inp.to_string()
            .lines()
            .filter(|line| {
                let report = line
                    .split_whitespace()
                    .filter_map(|x| x.parse::<isize>().ok())
                    .collect::<Vec<_>>();
                let mut increasing = false;

                !report.array_windows::<2>()
                    .enumerate()
                    .any(|(i, [a, b])| {
                        let jump = b - a;

                        if i == 0 {
                            increasing = jump > 0;
                        }

                        !(1..=3).contains(&if increasing { jump } else { -jump })
                    })
            })
            .count()
    }

    fn part_two<T: Display>(&self, inp: T) -> Self::OutputP2 {
        inp.to_string()
            .lines()
            .filter(|line| {
                (0..line.len()).any(|remove| {
                    let report = line
                        .split_whitespace()
                        .enumerate()
                        .filter_map(|(i, x)| x.parse::<isize>().ok().filter(|_| i != remove))
                        .collect::<Vec<_>>();
                    let mut increasing = false;

                    !report.array_windows::<2>()
                        .enumerate()
                        .any(|(i, [a, b])| {
                            let jump = b - a;

                            if i == 0 {
                                increasing = jump > 0;
                            }

                            !(1..=3).contains(&if increasing { jump } else { -jump })
                        })
                })
            })
            .count()
    }

    fn run(&self, inp: String) {
        let p1 = self.part_one(&inp);
        let p2 = self.part_two(&inp);

        println!("Part 1: {p1}");
        println!("Part 2: {p2}");

        assert_eq!(p1, 585);
        assert_eq!(p2, 626);
    }
}

fn main() {
    aoc_2024::run_day(2, &Day2);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}