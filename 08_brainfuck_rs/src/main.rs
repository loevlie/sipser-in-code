use std::io::{self, Read, Write};
use std::{env, fs, process};

fn main() {
    let args: Vec<String> = env::args().collect();
    let Some(path) = args.get(1) else {
        eprintln!("usage: brainfuck <program.bf>");
        process::exit(2);
    };

    let program = match fs::read(path) {
        Ok(bytes) => bytes,
        Err(e) => {
            eprintln!("failed to read {path}: {e}");
            process::exit(1);
        }
    };

    let stdin = io::stdin();
    let stdout = io::stdout();
    let mut input = stdin.lock();
    let mut output = stdout.lock();

    if let Err(e) = brainfuck::run(&program, &mut input, &mut output) {
        let _ = writeln!(io::stderr(), "runtime error: {e}");
        process::exit(1);
    }

    // Drop the stream guards before exit so the trailing newline (if any) flushes.
    drop(output);
    let _ = input.read_to_end(&mut Vec::new()); // eat any trailing input, ignore
}
