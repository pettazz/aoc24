package main

import (
  "bytes"
  "fmt"
  "os"
  "strings"
)

func main() {
  input, err := os.ReadFile("input.txt")
  if err != nil { panic(err) }
  rows := strings.Split(string(input), "\n")
  if rows[len(rows)-1] == "" {
    rows = rows[:len(rows)-1]
  }

  count := 0

  for idx, row := range rows {
    for stridx := 0; stridx < len(row); {
      xpos := strings.Index(row[stridx:], "X")
      if xpos == -1 {
        break
      } else {
        xpos += stridx
      }

      for m := -1; m < 2; m++ {
        for n := -1; n < 2; n++ {
          var foundstr bytes.Buffer
          foundstr.WriteString("X")
          for c := 1; c < 4; c++ {
            x := idx+c*m
            y := xpos+c*n
            if (x > -1 && x < len(rows)) && (y > -1 && y < len(row)) {
              foundstr.WriteString(string(rows[x][y]))
            }
          }

          if foundstr.String() == "XMAS" {
            count++
          }
        }
      }
      stridx = xpos + 1
    }
  }

  fmt.Println(int(count))
}