def part_1():
  input = open('13_input.txt', 'r')
  earliest = int(input.readline())
  buses = input.readline().strip().split(',')
  buses = [int(b) for b in filter(lambda b: b != 'x', buses)]
  print(buses)

  min_wait = earliest
  min_bus = 0
  for bus in buses:
    wait = bus - (earliest % bus)
    if wait < min_wait:
      min_wait = wait
      min_bus = bus
  print(min_wait, min_bus)
  return min_wait * min_bus

def part_2():
  return # rip
