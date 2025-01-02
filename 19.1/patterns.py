possible = 0
patterns = []
sequences = []
with open("input.txt") as f:
  patterns = f.readline().strip().split(", ")
  f.readline()
  for line in f:
    sequences.append(line.strip())

def matchPatternsIn(sequence):
  if sequence == "":
    return True
  matches = []
  for patt in patterns:
    if sequence.startswith(patt):
      matches.append(patt)

  if len(matches) > 0:
    return any(matchPatternsIn(sequence.removeprefix(p)) for p in matches)
  else:
    return False

for seq in sequences:
  if matchPatternsIn(seq):
    possible += 1
print(possible)