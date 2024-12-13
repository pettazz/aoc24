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

freep = 1
filep = len(diskmap) - 1
while filep > freep:
  freesize = diskmap[freep][1]
  filesize = diskmap[filep][1]
  fileid = diskmap[filep][0]

  if not freesize > 0:
    freep += 2
  elif not filesize > 0:
    filep +=2
  else:
    if freesize == filesize:
      diskmap[freep] = (fileid, freesize)
      diskmap[filep] = (-1, filesize)
      
      freep += 2
      filep = filep - 2
    elif freesize > filesize:
      diskmap[freep] = (fileid, filesize)
      diskmap[filep] = (-1, filesize)
      freeremainder = freesize - filesize
      diskmap.insert(freep+1, (-1, freeremainder))

      freep += 1
      filep = filep - 1
    else:
      diskmap[freep] = (fileid, freesize)
      fileremainder = filesize - freesize
      diskmap[filep] = (fileid, fileremainder)
      diskmap.insert(filep+1, (-1, freesize))

      freep += 2

checksum = 0
pos = 0
for block in diskmap:
  nextpos = pos + block[1]
  for i in range(pos, nextpos):
    if block[0] > -1:
      checksum += i * block[0]
  pos = nextpos

print(checksum)
