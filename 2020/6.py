def solve(group_accumulator):
  input = open('6_input.txt', 'r')
  total_count = 0
  curr_group = None
  for line in input:
    if line == '\n' and curr_group is not None:
      total_count += len(curr_group)
      curr_group = None
    else:
      curr_person = set(list(line.strip()))
      curr_group = group_accumulator(curr_group, curr_person)
  total_count += len(curr_group)
  return total_count

def part_1_accumulator(curr_group, curr_person):
  curr_group = curr_group or set()
  return curr_group.union(curr_person)

def part_2_accumulator(curr_group, curr_person):
  if curr_group is None: # We are checking the first person of the group.
    return curr_person
  return curr_group.intersection(curr_person)

def part_1():
  return solve(part_1_accumulator)

def part_2():
  return solve(part_2_accumulator)
