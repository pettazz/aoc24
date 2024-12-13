with open("input.txt") as f:
  instones = f.read().replace("\n", "").split()

# yes this is just reinventing collections.Counter
# but won't somebody think of the translations 
def addnum(numlist, num, count=1):
  if num in numlist.keys():
    numlist[num] += count
  else:
    numlist[num] = count
  return numlist

def importstones(newstones):
  newnums = {}
  for stone in newstones:
    addnum(newnums, stone)
  return newnums

stonenums = importstones(instones)

for blink in range(75):
  newstones = {}
  for stone in list(stonenums.keys()):
    count = stonenums[stone]
    if stone == "0":
      newstones = addnum(newstones, "1", count)
    elif len(stone) % 2 == 0:
      newl = str(int(stone[:len(stone)//2]))
      newr = str(int(stone[len(stone)//2:]))

      newstones = addnum(newstones, newl, count)
      newstones = addnum(newstones, newr, count)
    else:
      newstones = addnum(newstones, str(int(stone) * 2024), count)
  stonenums = newstones
  # print([(stone, count) for stone, count in stonenums.items() if count > 0])  


print(sum(stonenums.values()))