use std::fs::read_to_string;

fn main() {
    let mut count = 0;
    let rows: Vec<String> = read_to_string("input.txt")  
        .unwrap()
        .lines()
        .filter(|l| !l.trim().is_empty())
        .map(|l| l.to_string())
        .collect();

    for idx in 0..rows.len() {
        let row = &rows[idx];
        let mut stridx = 0;

        while stridx < row.len() {
            let xpos;
            let searchstr = &row[stridx..];
            if let Some(findx) = searchstr.find('X') {
                xpos = stridx + findx;
            } else {
                break;
            }

            for m in -1i32..2 {
                for n in -1i32..2 {
                    let mut foundstr = "X".to_owned();
                    for c in 1i32..4 {
                        let x = (idx as i32) + c * m;
                        let y = (xpos as i32) + c * n;

                        // much better thing to do in rust would have been also breaking each row
                        // into a list instead of trying to do string stuff that it doesn't like
                        // but hey this is about learning how these languages do things so OKAY
                        if (x > -1 && x < rows.len() as i32) && (y > -1 && y < row.len() as i32) {
                            foundstr.push_str(&rows[x as usize][y as usize..y as usize + 1]);
                        }
                    }

                    if foundstr == "XMAS" {
                        count += 1;
                    }
                }
            }

            stridx = xpos + 1;
        }
    }

    println!("{:?}", count);
}