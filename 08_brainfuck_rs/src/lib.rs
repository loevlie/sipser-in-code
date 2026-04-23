//! Brainfuck interpreter core.
//!
//! The program is a `&[u8]`; the tape is a `Vec<u8>` that grows on demand.
//! Bracket matching is precomputed up front so the hot loop never scans.

use std::io::{Read, Write};

pub const TAPE_SIZE: usize = 30_000;

/// Return a map from every `[` / `]` index to its matching partner.
pub fn match_brackets(program: &[u8]) -> Result<Vec<usize>, String> {
    // TODO: linear scan with a Vec<usize> stack.
    let _ = program;
    unimplemented!()
}

/// Run a Brainfuck program with the given input/output streams.
pub fn run<R: Read, W: Write>(
    program: &[u8],
    input: &mut R,
    output: &mut W,
) -> Result<(), String> {
    let _ = (program, input, output);
    // TODO: classic `match` over the 8 instructions inside a `while ip < len` loop.
    unimplemented!()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    #[ignore = "skeleton: implement run() first"]
    fn hello_world_runs() {
        let program = include_bytes!("../examples/hello.bf");
        let mut out = Vec::new();
        run(program, &mut std::io::empty(), &mut out).unwrap();
        assert!(String::from_utf8(out).unwrap().contains("Hello"));
    }
}
