import Foundation

let inputText = try! String(contentsOfFile: "input.txt", encoding: String.Encoding.utf8)
let rows = inputText.components(separatedBy: CharacterSet.newlines).filter { !$0.isEmpty }

var count = 0

for (idx, row) in rows.enumerated() {
  var stridx = 0;

  while stridx < row.count {
    var xpos: Int;

    let searchstr = row[row.index(row.startIndex, offsetBy: stridx)...]
    if let findx = searchstr.firstIndex(of: "X")?.encodedOffset {
      xpos = findx
    } else {
      break
    }

    for m in -1..<2 {
      for n in -1..<2 {
        var foundstr = "X"
        for c in 1..<4 {
          let x = idx+c*m
          let y = xpos+c*n

          if (x > -1 && x < rows.count) && (y > -1 && y < row.count) {
            // wow the string indexing stuff is also unpleasant in swift
            // definitely should have done an array here too oh well!
            foundstr += rows[x][row.index(row.startIndex, offsetBy: y)...row.index(row.startIndex, offsetBy: y)]
          }
        }

        if foundstr == "XMAS" {
          count += 1
        }
      }
    }
    
    stridx = xpos + 1
  }
}

print(count)