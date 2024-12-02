package main

import (
  "fmt"
  "os"
  "slices"
  "strconv"
  "strings"
)

func main() {
  input, err := os.ReadFile("input.txt")
  if err != nil { panic(err) }

  lines := strings.Split(string(input), "\n")
  l := make([]float64, len(lines), len(lines))
  r := make([]float64, len(lines), len(lines))

  for idx, line := range lines {
    if len(line) == 0 { break }
    vals := strings.Split(line, "   ")
    l[idx], _ = strconv.ParseFloat(vals[0], 64)
    r[idx], _ = strconv.ParseFloat(vals[1], 64)
  }

  slices.Sort(l)
  slices.Sort(r)

  total := 0.0
  ridx := 0
  for lidx := range l {
    rcount := 0

    for ; r[ridx] < l[lidx]; ridx++ { }

    for ; r[ridx] == l[lidx]; ridx++ {
      rcount++
    }

    total += l[lidx] * float64(rcount)
  }

  fmt.Println(int(total))
}