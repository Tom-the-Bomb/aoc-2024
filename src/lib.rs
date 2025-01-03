#![feature(associated_type_defaults)]

use std::{
    time::Instant,
    fs::read_to_string
};

pub use solution::*;
pub use util::*;

pub mod solution;
pub mod util;

/// # Panics
///
/// Will panic if failed to read input file for specified day for whatever reason
#[inline]
#[must_use]
pub fn get_input(day: u8) -> String {
    read_to_string(format!("./inputs/day{day}.txt"))
        .unwrap_or_else(|_| panic!("Failed to read input for Day {day}"))
}

pub fn run_day<D: Solution>(day: u8, cls: &D) {
    let text = format!(" Day [{day}] Solution - {} ", cls.name());
    let line = format!(
        "+------+{}+",
        "-".repeat(text.chars().count())
    );
    println!("\n{line}\n| RUST |{text}|\n{line}");

    let input = get_input(day);
    // benchmark and run
    let instant = Instant::now();
    cls.run(input);
    let text = format!("Execution time: {:?}", instant.elapsed());
    println!(
        "{text}\n{}",
        "=".repeat(text.chars().count())
    );
}