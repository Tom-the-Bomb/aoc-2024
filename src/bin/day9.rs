//! Day 9: Disk Fragmenter
//!
//! <https://adventofcode.com/2024/day/9>

use std::fmt::Display;
use aoc_2024::Solution;

pub struct Day9;

impl Solution for Day9 {
    const NAME: &'static str = "Disk Fragmenter";

    fn part_one<T: Display>(&self, inp: T) -> usize {
        let mut disk = Vec::new();
        let mut num = 0;

        for (i, count) in inp
            .to_string()
            .bytes()
            .enumerate()
        {
            let count = count as usize - 48;

            if i % 2 == 0 {
                disk.extend_from_slice(&vec![Some(num); count]);
                num += 1;
            } else {
                disk.extend_from_slice(&vec![None; count]);
            }
        }

        let mut i = 0;

        while i < disk.len() {
            if disk[i].is_none() {
                if let Some(last @ Some(_)) = disk.pop() {
                    disk[i] = last;
                } else {
                    continue;
                }
            }
            i += 1;
        }

        disk.into_iter()
            .enumerate()
            .filter_map(|(i, num)| num.map(|n| n * i))
            .sum()
    }

    fn part_two<T: Display>(&self, inp: T) -> usize {
        let mut disk = Vec::new();
        let mut spaces = Vec::new();
        let mut blocks = Vec::new();

        let mut num = 0usize;

        for (i, count) in inp
            .to_string()
            .bytes()
            .enumerate()
        {
            let count = count as usize - 48;
            let start = disk.len();
            let interval = start..start + count;

            if i % 2 == 0 {
                let block = vec![Some(num); count];

                disk.extend_from_slice(&block);
                blocks.push((block, interval));
                num += 1;
            } else {
                spaces.push(interval);
                disk.extend_from_slice(&vec![None; count]);
            }
        }

        for (block, block_interval) in blocks
            .into_iter()
            .rev()
        {
            let block_size = block_interval.len();

            for space in &mut spaces {
                let space_size = space.len();

                if block_size <= space_size && space.start < block_interval.start {
                    disk[block_interval].fill(None);
                    disk[space.start..space.start + block_size].copy_from_slice(&block);

                    space.start += block_size;
                    break;
                }
            }
        }

        disk.into_iter()
            .enumerate()
            .filter_map(|(i, num)| num.map(|n| n * i))
            .sum()
    }

    fn run(&self, inp: String) {
        let p1 = self.part_one(&inp);
        let p2 = self.part_two(&inp);

        println!("Part 1: {p1}");
        println!("Part 2: {p2}");

        assert_eq!(p1, 6_356_833_654_075);
        assert_eq!(p2, 6_389_911_791_746);
    }
}

fn main() {
    aoc_2024::run_day(9, &Day9);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test() { main(); }
}