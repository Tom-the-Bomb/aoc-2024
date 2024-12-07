//! Day 7: Bridge Repair
//!
//! <https://adventofcode.com/2024/day/7>

use std::fmt::Display;
use aoc_2024::Solution;

pub struct Day7;

impl Day7 {
    fn solve_p1(target: usize, terms: &[usize], curr: usize, progression: usize) -> bool {
        if progression == terms.len() {
            return target == curr;
        }

        let term = terms[progression];

        Self::solve_p1(
            target,
            terms,
            curr + term,
            progression + 1
        ) || Self::solve_p1(
            target,
            terms,
            curr * term,
            progression + 1
        )
    }

    #[allow(
        clippy::cast_sign_loss,
        clippy::cast_precision_loss,
        clippy::cast_possible_truncation,
    )]
    fn solve_p2(target: usize, terms: &[usize], curr: usize, progression: usize) -> bool {
        if progression == terms.len() {
            return target == curr;
        }

        let term = terms[progression];

        Self::solve_p2(
            target,
            terms,
            curr + term,
            progression + 1,
        ) || Self::solve_p2(
            target,
            terms,
            curr * term,
            progression + 1,
        ) || Self::solve_p2(
            target,
            terms,
            curr * (10usize).pow((term as f64).log10() as u32 + 1) + term,
            progression + 1,
        )
    }
}

impl Solution for Day7 {
    const NAME: &'static str = "Bridge Repair";

    fn part_one<T: Display>(&self, inp: T) -> usize {
        inp.to_string()
            .lines()
            .filter_map(|equation| {
                let (target, terms) = equation.split_once(':').unwrap();

                let mut terms = terms
                    .split_whitespace()
                    .filter_map(|term| term.parse::<usize>().ok());
                let first = terms
                    .next()
                    .unwrap();
                let terms = terms
                    .collect::<Vec<_>>();
                let target = target
                    .parse()
                    .unwrap();

                Self::solve_p1(target, &terms, first, 0)
                    .then_some(target)
            })
            .sum()
    }

    fn part_two<T: Display>(&self, inp: T) -> usize {
        inp.to_string()
            .lines()
            .filter_map(|equation| {
                let (target, terms) = equation.split_once(':').unwrap();

                let mut terms = terms
                    .split_whitespace()
                    .filter_map(|term| term.parse::<usize>().ok());
                let first = terms
                    .next()
                    .unwrap();
                let terms = terms
                    .collect::<Vec<_>>();
                let target = target
                    .parse()
                    .unwrap();

                Self::solve_p2(target, &terms, first, 0)
                    .then_some(target)
            })
            .sum()
    }

    fn run(&self, inp: String) {
        let p1 = self.part_one(&inp);
        let p2 = self.part_two(&inp);

        println!("Part 1: {p1}");
        println!("Part 2: {p2}");

        assert_eq!(p1, 3_351_424_677_624);
        assert_eq!(p2, 204_976_636_995_111);
    }
}

fn main() {
    aoc_2024::run_day(7, &Day7);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}