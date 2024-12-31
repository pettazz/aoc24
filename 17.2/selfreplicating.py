registers = {
  "A": 0,
  "B": 0,
  "C": 0
}
program = []

with open("input.txt") as f:
  for line in f:
    if line.strip() == "":
      continue
    if line.startswith("Register"):
      rvals = line.split("Register ")[1].split(":")
      registers[rvals[0]] = int(rvals[1].strip())
    if line.startswith("Program"):
      program = [int(x) for x in line.split(": ")[1].strip().split(",")]

def runProgram(program, registers):
  output = []
  ip = 0
  while ip+1 < len(program):
    opcode = program[ip]
    operand = program[ip+1]

    if operand == 7 and opcode not in [1, 3, 4]:
      raise ValueError("invalid combo operand 7 with opcode `%s`" % opcode)

    if operand in [0, 1, 2, 3, 7]:
      opval = operand
    elif operand in [4, 5, 6]:
      opval = registers[["A", "B", "C"][operand-4]]
    else:
      raise ValueError("unknown operand `%s`" % operand)

    if opcode == 0:
      # adv - division into reg a
      numerator = registers["A"]
      denominator = pow(2, opval)

      registers["A"] = numerator // denominator

    if opcode == 1:
      # bxl - bitwise or
      val1 = registers["B"]
      val2 = opval 

      registers["B"] = val1 ^ val2

    if opcode == 2:
      # bst - 3 lower bits
      registers["B"] = opval % 8

    if opcode == 3:
      # jnz - jump
      if registers["A"] != 0:
        ip = opval
        continue

    if opcode == 4:
      # bxc - bitwise or in regs
      registers["B"] = registers["B"] ^ registers["C"]

    if opcode == 5:
      # out - output
      output.append(str(opval % 8))

    if opcode == 6:
      # bdv - division into reg b 
      numerator = registers["A"]
      denominator = pow(2, opval)

      registers["B"] = numerator // denominator

    if opcode == 7:
      # cdv - division into reg c
      numerator = registers["A"]
      denominator = pow(2, opval)

      registers["C"] = numerator // denominator

    ip += 2

  return output

def findReplicatingA(program):
  foundA = 0
  for i in range(1, len(program)+1):
    backChunk = [str(x) for x in program[len(program)-i:]]
    inc = 0
    while True:
      # this doesnt seem like it should work but ok
      testa = (foundA << 3) + inc
      result = runProgram(program, {"A": testa, "B": 0, "C": 0})
      if result == backChunk:
        foundA = testa
        break
      inc += 1
  return foundA

print(findReplicatingA(program))