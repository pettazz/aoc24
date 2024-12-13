diskmap = []

with open("input.txt") as f:
  compactmap = f.read().replace("\n", "")

  for idx, char in enumerate(compactmap):
    size = int(char)
    if idx % 2 == 0:
      # file
      diskmap.append((idx // 2, size))
    else:
      # empty space
      diskmap.append((-1, size))


for i in range(1, len(diskmap)):
  filep = -1 * i

  if diskmap[filep][0] == -1:
    continue

  filesize = diskmap[filep][1]
  fileid = diskmap[filep][0]

  for freep in range(1, len(diskmap) + filep):
    if diskmap[freep][0] == -1:
      freesize = diskmap[freep][1]
      
      if freesize > 0:
        if freesize == filesize:
          diskmap[freep] = (fileid, filesize)
          diskmap[filep] = (-1, filesize)
          break
          
        if freesize > filesize:
          diskmap[freep] = (fileid, filesize)
          diskmap[filep] = (-1, filesize)
          freeremainder = freesize - filesize
          diskmap.insert(freep+1, (-1, freeremainder))
          break

checksum = 0
pos = 0
for block in diskmap:
  nextpos = pos + block[1]
  for i in range(pos, nextpos):
    if block[0] > -1:
      checksum += i * block[0]
  pos = nextpos

print(checksum)