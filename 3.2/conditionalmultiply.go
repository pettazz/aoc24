package main

import (
  "fmt"
  "os"
  "regexp"
  "strconv"
  "strings"
)

func domuls(block string) uint32 {
  total := 0;

  r := regexp.MustCompile(`mul\(([0-9]{1,3}),([0-9]{1,3})\)`)
  ops := r.FindAllStringSubmatch(block, -1)
  for _, op := range ops {
    l, _ := strconv.Atoi(op[1])
    r, _ := strconv.Atoi(op[2])
    total += l * r
  }

  return uint32(total)
}

func main() {
  input, err := os.ReadFile("input.txt")
  if err != nil { panic(err) }

  var total uint32 = 0
  memory := strings.Replace(string(input), "\n", "", -1)

  dos := strings.Split(memory, "do()")
  blocks := make([]string, 1)
  for _, do := range dos {
    donts := strings.SplitN(do, "don't()",  2)
    blocks = append(blocks, donts[0])
  }

  for _, block := range blocks {
    total += domuls(block) 
  }

  fmt.Println(int(total))
}