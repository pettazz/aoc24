package main

import (
  "fmt"
  "math"
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
  for idx := range l {
    total += math.Abs(l[idx] - r[idx])
  }

  fmt.Println(int(total))
}