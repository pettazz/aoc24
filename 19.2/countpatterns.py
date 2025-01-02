possible = 0
patterns = []
sequences = []
with open("input.txt") as f:
  patterns = f.readline().strip().split(", ")
  f.readline()
  for line in f:
    sequences.append(line.strip())

# someday someone is going to explain the word `memoize` to me
# but until then i will just keep calling it caching
cache = {}

def matchPatternsIn(sequence):
  if sequence in cache.keys():
    return cache[sequence]
  if sequence == "":
    return 1
  matches = []
  for patt in patterns:
    if sequence.startswith(patt):
      matches.append(patt)

  if len(matches) > 0:
    result = sum(matchPatternsIn(sequence.removeprefix(p)) for p in matches)
    cache[sequence] = result
    return result
  else:
    return 0

for seq in sequences:
  possible += matchPatternsIn(seq)
print(possible)