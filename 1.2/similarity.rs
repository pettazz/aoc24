use std::fs::read_to_string;

fn parse_lines() -> (Vec<i32>, Vec<i32>){
    let mut l = Vec::new();
    let mut r = Vec::new();

    for line in read_to_string("input.txt").unwrap().lines() {
        let Some((left, right)) = line.split_once("   ") else { panic!("Bad input line!") };
        l.push(left.parse::<i32>().unwrap());
        r.push(right.parse::<i32>().unwrap());
    }

    l.sort();
    r.sort();

    return (l, r);
}

fn main() {
    let lists = parse_lines();

    let mut total = 0;
    for lidx in 0..lists.0.len() {
        let mut rcount = 0;
        let mut ridx = 0;

        while lists.1[ridx] < lists.0[lidx] {
            ridx += 1;
        }

        while lists.1[ridx] == lists.0[lidx] {
            rcount += 1;
            ridx += 1;
        }

        total += lists.0[lidx] * rcount;
    }

    println!("{:?}", total);
}