import Foundation

let inputText = try! String(contentsOfFile: "input.txt", encoding: String.Encoding.utf8)
let lines = inputText.components(separatedBy: CharacterSet.whitespacesAndNewlines)

var l: [Int] = []
var r: [Int] = []

for i in 0..<lines.count {
  if (lines[i]) == "" {
    continue
  }
  if i % 2 == 0 {
    l.append(Int(lines[i])!)
  } else {
    r.append(Int(lines[i])!)
  }
}

l.sort()
r.sort()

var total = 0, ridx = 0;

for lidx in 0..<l.count {
  var rcount = 0;

  while r[ridx] < l[lidx] {
    ridx += 1;
  }

  while r[ridx] == l[lidx] {
    rcount += 1;
    ridx += 1;
  }

  total += l[lidx] * rcount
}

print(total)