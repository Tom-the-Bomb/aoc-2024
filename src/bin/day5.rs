//! Day 5: Print Queue
//!
//! <https://adventofcode.com/2024/day/5>

use std::{collections::HashMap, fmt::Display};
use aoc_2024::Solution;

pub struct Day5;

macro_rules! parse_input {
    ($inp:expr) => {{
        let (rules, updates) = $inp
            .split_once("\n\n")
            .unwrap();
        (
            rules.lines()
                .filter_map(|rule| rule.split_once('|'))
                .collect::<Vec<_>>(),
            updates.lines()
                .map(|rule| rule.split(',').collect::<Vec<_>>())
                .collect::<Vec<_>>()
        )
    }}
}

impl Solution for Day5 {
    const NAME: &'static str = "Print Queue";

    fn part_one<T: Display>(&self, inp: T) -> Self::OutputP1 {
        let inp = inp.to_string().replace('\r', "");
        let (rules, updates) = parse_input!(inp);
        let mut total = 0;

        'a: for update in updates {
            let mut indices = HashMap::with_capacity(update.len());

            for (i, &page) in update.iter().enumerate() {
                indices.insert(page, i);
            }

            for (a, b) in &rules {
                match (indices.get(a), indices.get(b)) {
                    (Some(i), Some(j)) if i > j => continue 'a,
                    _ => (),
                }
            }

            total += update[update.len() / 2]
                .parse::<usize>()
                .unwrap();
        }
        total
    }

    fn part_two<T: Display>(&self, inp: T) -> Self::OutputP2 {
        let inp = inp.to_string().replace('\r', "");
        let (rules, updates) = parse_input!(inp);
        let mut total = 0;

        for mut update in updates {
            let mut indices = HashMap::with_capacity(update.len());

            for (i, &page) in update.iter().enumerate() {
                indices.insert(page, i);
            }

            let mut counter = HashMap::new();
            let mut invalid = false;

            for (a, b) in &rules {
                if let (Some(i), Some(j)) = (indices.get(a), indices.get(b)) {
                    *counter.entry(a).or_insert(0) += 1;

                    if i > j {
                        invalid = true;
                    }
                }
            }

            if invalid {
                update.sort_unstable_by_key(|page| -counter.get(page).unwrap_or(&0));
                total += update[update.len() / 2]
                    .parse::<usize>()
                    .unwrap();
            }
        }
        total
    }

    fn run(&self, inp: String) {
        let p1 = self.part_one(&inp);
        let p2 = self.part_two(&inp);

        println!("Part 1: {p1}");
        println!("Part 2: {p2}");

        assert_eq!(p1, 4872);
        assert_eq!(p2, 5564);
    }
}

fn main() {
    aoc_2024::run_day(5, &Day5);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}