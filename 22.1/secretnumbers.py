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

total = 0
for s in startNums:
  for i in range(2000):
    s = genSecretFrom(s)
  total += s

print(total)