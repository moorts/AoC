mod day2 {
    use std::{collections::{HashMap, HashSet}, fs::{self, File}, io::{BufReader, BufRead}};
    #[test]
    fn run() {
        let lines = BufReader::new(File::open("./src/day2/input").expect("fuck")).lines();
        let mut l = Vec::new();
        for line in lines {
            if let Ok(s) = line {
                l.push(s);
            }
        }
        'outer: for i in 0..l.len() {
            for j in i+1..l.len() {
                if let Ok(s) = compare(&l[i], &l[j]) {
                    println!("Found: {}", s);
                    break 'outer;
                }
            }
        }
        assert!(false);
    }

    fn compare(s1: &String, s2: &String) -> Result<String, &'static str> {
        let mut i = 0;
        let mut matches = 0;
        let v1: Vec<char> = s1.chars().collect();
        let v2: Vec<char>  = s2.chars().collect();
        let mut res = String::new();
        while i < v1.len() {
            let (c1, c2) = (v1[i], v2[i]);
            if c1 != c2 {
                if matches == 0 {
                    matches = 1;
                } else {
                    return Err("Nope");
                }
            } else {
                res += &c1.to_string();
            }
            i += 1;
        }
        if matches == 1 {
            return Ok(res);
        }
        Err("Nope")
    }

    fn count(s: String) -> (usize, usize) {
        let mut occs = HashMap::new();
        for c in s.chars() {
            let count = occs.entry(c).or_insert(0);
            *count += 1;
        }
        println!("{:?}", occs);

        let mut i = 0 as usize;
        let mut j = 0 as usize;
        for (key, occ) in occs {
            if occ == 2 {
                i = 1;
            } else if occ == 3 {
                j = 1;
            }
        }
        (i, j)
    }
}
