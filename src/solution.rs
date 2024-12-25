use std::fmt::Display;

pub trait Solution {
    const NAME: &'static str;

    type OutputP1 = usize;
    type OutputP2 = usize;

    fn part_one<T: Display>(&self, inp: T) -> Self::OutputP1;

    fn part_two<T: Display>(&self, inp: T) -> Self::OutputP2;

    fn run(&self, inp: String);

    #[inline]
    #[must_use]
    fn name(&self) -> &'static str {
        Self::NAME
    }
}