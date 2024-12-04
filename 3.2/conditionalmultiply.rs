use std::fs::read_to_string;
// need a cargo add to run this one
use regex::Regex;

fn domuls(memory: String) -> i32 {
    let mut total = 0;
    let r = Regex::new(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)").unwrap();

    for (_, [l, r]) in r.captures_iter(&memory).map(|m| m.extract()) {
        total += l.parse::<i32>().unwrap() * r.parse::<i32>().unwrap();
    }

    return total;
}

fn main() {
    let mut memory: String = "".to_owned();
    for line in read_to_string("../input.txt").unwrap().lines() {
        memory.push_str(line);
    }

    let mut ops = Vec::new();
    for ado in memory.split("do()") {
        let dont = ado.split_once("don't()");
         match dont {
            Some(dont) => {
                ops.push(dont.0.to_string());
            },
            None => {
                ops.push(ado.to_string());
            }
         }
    }

    let mut total = 0;
    for op in ops {
        total += domuls(op);
    }

    println!("{:?}", total);
}