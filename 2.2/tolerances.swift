import Foundation

func isReportOk(_ report: [Int], _ tolerance: Int) -> Bool {
  for i in 0..<report.count - 1 {
    let diff = report[i] - report[i+1]
    if !(diff > 0 && diff < 4) {
      if tolerance > 0 {
        let prevChar = i - 1 >= 0 ? i - 1 : 0
        if !(isReportOk(Array(report[prevChar..<i]) + Array(report[(i+1)...]), tolerance - 1) ||
              isReportOk(Array(report[i..<(i+1)]) + Array(report[(i+2)...]), tolerance - 1)){
          return false
        }
      } else {
        return false
      }
    }
  }

  return true;
}

let inputText = try! String(contentsOfFile: "input.txt", encoding: String.Encoding.utf8)
let lines = inputText.components(separatedBy: CharacterSet.newlines)

var safe = 0, unsafe = 0

for line in lines {
  if line == "" {
    continue
  }

  let report = line.components(separatedBy: CharacterSet.whitespaces).map { Int($0)! }
  if isReportOk(report, 1) || isReportOk(report.reversed(), 1) {
    safe += 1
  } else {
    unsafe += 1
  }
}

print(String(format: "safe: %u, unsafe: %u", safe, unsafe))