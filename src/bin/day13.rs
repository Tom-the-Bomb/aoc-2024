//! Day 13: Claw Contraption
//!
//! <https://adventofcode.com/2024/day/13>

use std::fmt::Display;
use regex::{RegexBuilder, Regex};
use aoc_2024::Solution;

pub struct Day13;

lazy_static::lazy_static! {
    static ref MACHINE_PATTERN: Regex = RegexBuilder::new(
        r"Button A: X\+([0-9]+), Y\+([0-9]+)[\n\r]+Button B: X\+([0-9]+), Y\+([0-9]+)[\n\r]+Prize: X=([0-9]+), Y=([0-9]+)"
    )
        .build()
        .unwrap();
}

impl Day13 {
    #[allow(clippy::cast_sign_loss)]
    fn solve<T: Display>(inp: T, target_offset: isize) -> usize {
        MACHINE_PATTERN
            .captures_iter(&inp.to_string())
            .filter_map(|mat| {
                let [ax, ay, bx, by, mut target_x, mut target_y] = mat
                    .extract()
                    .1
                    .map(|group| group.parse::<isize>().unwrap());

                target_x += target_offset;
                target_y += target_offset;

                let b_presses = (ay * target_x - ax * target_y) / (ay * bx - ax * by);
                let a_presses = (target_x - bx * b_presses) / ax;

                (ax * a_presses + bx * b_presses == target_x && ay * a_presses + by * b_presses == target_y)
                    .then(|| 3 * a_presses + b_presses)
            })
            .sum::<isize>() as usize
    }
}

impl Solution for Day13 {
    const NAME: &'static str = "Claw Contraption";

    fn part_one<T: Display>(&self, inp: T) -> usize {
        Self::solve(inp, 0)
    }

    fn part_two<T: Display>(&self, inp: T) -> usize {
        Self::solve(inp, 10_000_000_000_000)
    }

    fn run(&self, inp: String) {
        let p1 = self.part_one(&inp);
        let p2 = self.part_two(&inp);

        println!("Part 1: {p1}");
        println!("Part 2: {p2}");

        assert_eq!(p1, 39996);
        assert_eq!(p2, 73_267_584_326_867);
    }
}

fn main() {
    aoc_2024::run_day(13, &Day13);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}