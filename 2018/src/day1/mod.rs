use std::{collections::HashSet, fs::{self, File}, io::{BufReader, BufRead}};

#[test]
fn run() {
    let lines = BufReader::new(File::open("./src/day1/input").expect("fuck")).lines();
    let mut nums = Vec::new();
    for line in lines {
        if let Ok(l) = line {
            nums.push(l.to_string().parse::<i32>().expect("fuck"));
        }
    }
    let mut freqs = HashSet::new();
    let mut freq = 0;
    'outer: loop {
        for x in &nums {
            if freqs.contains(&freq) {
                println!("Found: {}", freq);
                break 'outer;
            }
            freqs.insert(freq);
            freq += x;
        }
    }
    assert!(false);
}
