with open("input.txt") as f:
  stones = f.read().replace("\n", "").split()

for blink in range(25):
  idx = 0
  while idx < len(stones):
    stone = stones[idx]
    if stone == "0":
      stones[idx] = "1"
    elif len(stone) % 2 == 0:
      stones[idx] = str(int(stone[:len(stone)//2]))
      stones.insert(idx+1, str(int(stone[len(stone)//2:])))
      idx += 1
    else:
      stones[idx] = str(int(stone) * 2024)

    idx += 1

print(len(stones))