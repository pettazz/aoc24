use std::fs::read_to_string;

fn parse_lines() -> Vec<Vec<i8>>{
    let mut reports = Vec::new();

    for line in read_to_string("input.txt").unwrap().lines() {
        let report: Vec<i8> = line.split(" ")
                                   .map(|i| i.parse::<i8>().unwrap())
                                   .collect();
        reports.push(report);
    }

    return reports;
}

fn is_report_ok(report: Vec<i8>, tolerance: u8) -> bool {
    for i in 0..report.len() -1 {
        let diff = report[i] - report[i+1];
        if !(diff > 0 && diff < 4) {
            if tolerance > 0 {
                let (mut report_minus_idx, mut report_minus_idx_one) = (report.clone(), report.clone());
                report_minus_idx.remove(i);
                report_minus_idx_one.remove(i+1);
                if !(is_report_ok(report_minus_idx, tolerance - 1) || is_report_ok(report_minus_idx_one, tolerance - 1)) {
                    return false;
                }
            } else {
                return false;
            }
        }
    }

    return true;
}

fn main() {
    let reports = parse_lines();

    let (mut safe, mut notsafe) = (0, 0);
    for idx in 0..reports.len() {
        let mut report_rev = reports[idx].clone();
        report_rev.reverse();
        if is_report_ok(reports[idx].clone(), 1) || is_report_ok(report_rev, 1) {
            safe += 1;
        } else {
            notsafe += 1;
        }
    }

    println!("safe: {:?}, unsafe: {:?}", safe, notsafe);
}