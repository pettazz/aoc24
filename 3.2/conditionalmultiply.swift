import Foundation

func domuls(_ block: String) -> Int {
  var total = 0

  // what is happening here why dont regular regexes work for me i am going insane
  let blockRange = NSRange(
    block.startIndex..<block.endIndex,
    in: block
  )
  let regex = try! NSRegularExpression(pattern: "mul\\((?<l>[0-9]{1,3}),(?<r>[0-9]{1,3})\\)")
  for op in regex.matches(in: block, range: blockRange) {
    var captures: [Int] = []
    for name in ["l", "r"] {
      let matchRange = op.range(withName: name)
      
      if let blockRange = Range(matchRange, in: block) {
        let capture = Int(block[blockRange])!
        captures.append(capture)
      }
    }
    total += captures[0] * captures[1]
  }

  return total
}

let memory = try! String(contentsOfFile: "input.txt", encoding: String.Encoding.utf8)
var total = 0

for ado in memory.split(separator: "do()") {
  let block = String(ado.split(separator: "don't()", maxSplits: 1)[0])
  total += domuls(block)
}

print(total)