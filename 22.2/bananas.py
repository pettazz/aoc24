def mix(a, b):
  return a ^ b

def prune(a):
  return a % 16777216

def genSecretFrom(s):  
  s = mix(s, s * 64)
  s = prune(s)
  s = mix(s, s // 32)
  s = prune(s)
  s = mix(s, s * 2048)
  s = prune(s)
  
  return s

startNums = []
with open("input.txt") as f:
  for line in f:
    if line.strip != "" and not line.startswith("#"):
      startNums.append(int(line.strip()))

total = {}
for s in startNums:
  seen = set()
  seq = (0, 0, 0, 0)
  for i in range(2000):
    prevPrice = s % 10
    s = genSecretFrom(s)

    price = s % 10
    diff = price - prevPrice
    seq = seq[1:] + (diff,)

    if i >= 3 and seq not in seen:
      if seq not in total.keys():
        total[seq] = price
      else:
        total[seq] += price
      seen.add(seq)
    prevPrice = price

bestSeq = max(total, key=total.get)
print(bestSeq, total[bestSeq])