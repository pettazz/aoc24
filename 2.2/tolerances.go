package main

import (
  "fmt"
  "os"
  "slices"
  "strconv"
  "strings"
)

func isReportOk(report []int, tolerance int) bool {
  for i := 0; i < len(report) - 1; i++ {
    diff := report[i] - report[i+1]
    if !(diff > 0 && diff < 4) {
      if tolerance > 0 {
        prevChar := i - 1
        if prevChar < 0 {
          prevChar = 0
        }

        if !(isReportOk(slices.Concat(report[prevChar:i], report[i+1:]), tolerance - 1) ||
             isReportOk(slices.Concat(report[i:i+1], report[i+2:]), tolerance - 1)) {
          return false
        }
      } else {
        return false
      }
    }

  }

  return true;
}

func main() {
  input, err := os.ReadFile("input.txt")
  if err != nil { panic(err) }

  lines := strings.Split(string(input), "\n")

  safe, unsafe := 0, 0

  for _, strline := range lines {
    if strline == "" {
      continue
    }
    strreport := strings.Split(strline, " ")
    report := make([]int, len(strreport))
    for idx, str := range strreport {
      report[idx], _ = strconv.Atoi(str)
    }
    reportRev := slices.Clone(report)
    slices.Reverse(reportRev)

    if isReportOk(report, 1) || isReportOk(reportRev, 1) {
      safe++
    } else {
      unsafe++
    }
  }

  fmt.Printf("safe: %v, unsafe: %v\n", safe, unsafe)
}