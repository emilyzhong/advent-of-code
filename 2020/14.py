def part_1():
  input = open('14_input.txt', 'r')
  memory = {}
  mask = 'X' * 36
  for line in input:
    left, right = line.strip().split(' = ')
    if left == 'mask':
      mask = right
    else:
      index = int(left.strip()[4:-1])
      prev_value = format(int(right.strip()), '036b')
      value = ''
      for i in range(len(mask)):
        if mask[i] != 'X':
          value += mask[i]
        else:
          value += prev_value[i]
      memory[index] = int(value, 2)
  return sum(list(memory.values()))

def possible_addresses(index, mask):
  floating = []
  prev_index, index = index, ''
  # apply initial mask + store floating indexes
  for i in range(len(mask)):
    if mask[i] == '1':
      index += '1'
    else:
      if mask[i] == 'X':
        floating.append(i)
      index += prev_index[i]

  possible_addresses = [index]
  for i in floating:
    zeros = [p[:i] + "0" + p[i+1:] for p in possible_addresses]
    ones = [p[:i] + "1" + p[i+1:] for p in possible_addresses]
    possible_addresses = zeros + ones

  possible_addresses = set([int(value, 2) for value in possible_addresses])
  return possible_addresses

def part_2():
  input = open('14_input.txt', 'r')
  memory = {}
  mask = 'X' * 36
  for line in input:
    left, right = line.strip().split(' = ')
    if left == 'mask':
      mask = right
    else:
      value = int(right.strip())
      index = format(int(left.strip()[4:-1]), '036b')
      indices = possible_addresses(index, mask)
      for i in indices:
        memory[i] = value
  return sum(list(memory.values()))
