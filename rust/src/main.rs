extern crate regex;

use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufWriter;
use regex::Regex;
use std::io;

fn iterate_codepoints(pattern: &str, file_path: &str) -> io::Result<()> {
    let file = File::create(file_path)?;
    let mut writer = BufWriter::new(file);
    let regex = Regex::new(pattern).unwrap();

    for i in 0..=0x10ffff {
        // if 0xd800 <= i && i <= 0xdfff {
        //     continue;
        // }
        let r = std::char::from_u32(i);
        if let Some(valid_char) = r {
            let char = valid_char.to_string();
            if regex.is_match(&char) {
                write!(writer, "{:04X}\n", i)?;
            }
        }
    }
    Ok(())
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 3 {
        println!("Usage: cargo run <pattern> <file_path>");
        return;
    }

    let pattern = &args[1];
    let file_path = &args[2];
    match iterate_codepoints(pattern, file_path) {
        Ok(()) => {},
        Err(e) => println!("Error: {}", e),
    }
}
