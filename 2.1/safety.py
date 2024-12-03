safe = 0
unsafe = 0

def isReportOk(report):
  trend = None
  
  for i in range(len(report) - 1):
    diff = int(report[i]) - int(report[i+1])
    if (diff > 0 and diff < 4) or (diff < 0 and diff > -4):
      if i == 0:
        trend = diff 
      else:
        if not ((trend > 0 and diff > 0) or (trend < 0 and diff < 0)):
          return False
    else:
      return False
  return True

with open('input.txt') as f:
  for line in f:
    if isReportOk(line.split()):
      safe += 1
    else:
      unsafe += 1

print("safe: %s, unsafe: %s" % (safe, unsafe))