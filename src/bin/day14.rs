//! Day 14: Mull It Over
//!
//! <https://adventofcode.com/2024/day/14>

use std::{
    collections::HashSet,
    cmp::Ordering,
    fmt::Display,
};
use regex::Regex;
use aoc_2024::Solution;

pub struct Day14;

impl Day14 {
    fn get_robots<T: Display>(inp: T) -> Vec<[isize; 4]> {
        Regex::new(r"p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)")
            .unwrap()
            .captures_iter(&inp.to_string())
            .map(|mat| {
                mat
                    .extract()
                    .1
                    .map(|group| group.parse::<isize>().unwrap())
            })
            .collect()
    }
}

impl Solution for Day14 {
    const NAME: &'static str = "Mull It Over";

    fn part_one<T: Display>(&self, inp: T) -> Self::OutputP1 {
        let robots = Self::get_robots(inp);

        let w = 101;
        let h = 103;

        let hw = w / 2;
        let hh = h / 2;

        let mut q1 = 0;
        let mut q2 = 0;
        let mut q3 = 0;
        let mut q4 = 0;

        for [mut x, mut y, vx, vy] in robots {
            x += 100 * vx;
            y += 100 * vy;

            x = x.rem_euclid(w);
            y = y.rem_euclid(h);

            match (x.cmp(&hw), y.cmp(&hh)) {
                (Ordering::Less, Ordering::Less) => q1 += 1,
                (Ordering::Less, Ordering::Greater) => q2 += 1,
                (Ordering::Greater, Ordering::Less) => q3 += 1,
                (Ordering::Greater, Ordering::Greater) => q4 += 1,
                _ => (),
            }
        }
        q1 * q2 * q3 * q4
    }

    fn part_two<T: Display>(&self, inp: T) -> Self::OutputP2 {
        let robots = Self::get_robots(inp);

        let w = 101;
        let h = 103;

        let mut t = 0;

        loop {
            let positions = robots
                .iter()
                .map(|[x, y, vx,  vy]| ((x + t * vx).rem_euclid(w), (y + t * vy).rem_euclid(h)))
                .collect::<Vec<_>>();

            if positions.len() == HashSet::<(isize, isize)>::from_iter(positions).len() {
                #[allow(clippy::cast_sign_loss)]
                break t as usize;
            }
            t += 1;
        }
    }

    fn run(&self, inp: String) {
        let p1 = self.part_one(&inp);
        let p2 = self.part_two(&inp);

        println!("Part 1: {p1}");
        println!("Part 2: {p2}");

        assert_eq!(p1, 230_436_441);
        assert_eq!(p2, 8270);
    }
}

fn main() {
    aoc_2024::run_day(14, &Day14);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}