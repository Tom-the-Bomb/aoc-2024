use std::fmt::Display;

#[must_use]
#[inline]
pub fn find_start(grid: &[Vec<u8>], char: u8) -> Option<(usize, usize)> {
    grid.iter()
        .enumerate()
        .find_map(|(i, row)| row
            .iter()
            .position(|&cell| cell == char)
            .map(|j| (i, j))
        )
}

#[must_use]
#[inline]
pub const fn neighbors_4(row: usize, col: usize) -> [(usize, usize); 4] {
    [
        (row, col.wrapping_sub(1)),
        (row, col.wrapping_add(1)),
        (row.wrapping_sub(1), col),
        (row.wrapping_add(1), col),
    ]
}

#[must_use]
#[inline]
pub const fn neighbors_diag(row: usize, col: usize) -> [(usize, usize); 4] {
    [
        (row.wrapping_sub(1), col.wrapping_sub(1)),
        (row.wrapping_sub(1), col.wrapping_add(1)),
        (row.wrapping_add(1), col.wrapping_sub(1)),
        (row.wrapping_add(1), col.wrapping_add(1)),
    ]
}

#[must_use]
pub fn gcd(a: usize, b: usize) -> usize {
    if b == 0 { a } else { gcd(b, a % b) }
}

#[must_use]
pub fn lcm<I>(nums: I) -> usize
where
    I: Iterator<Item = usize>,
{
    nums.fold(
        1,
        |num, ans| num * ans / gcd(num, ans),
    )
}

#[must_use]
#[inline]
pub fn get_grid<T: Display>(inp: T) -> Vec<Vec<u8>> {
    inp.to_string()
        .lines()
        .map(|line| line.as_bytes().to_vec())
        .collect::<Vec<_>>()
}