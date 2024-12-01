:: script for running the rust solutions
@ECHO off

cargo build --release
"./target/release/aoc-2024.exe" %1