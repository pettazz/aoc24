safe = 0
unsafe = 0

def isReportOk(report, tolerance = 1):
  for i in range(len(report) - 1):
    diff = report[i] - report[i+1]
    if not (4 > diff > 0):
      if tolerance > 0:
        prevChar = i - 1 if i - 1 >= 0 else 0
        if not (isReportOk(report[prevChar:i] + report[i+1:], tolerance - 1) or 
                isReportOk(report[i:i+1] + report[i+2:], tolerance - 1)):
          return False
      else:
        return False
  return True

with open('input.txt') as f:
  for line in f:
    report = [int(i) for i in line.split()]
    if isReportOk(report) or isReportOk(report[::-1]):
      safe += 1
    else:
      unsafe += 1

print("safe: %s, unsafe: %s" % (safe, unsafe))