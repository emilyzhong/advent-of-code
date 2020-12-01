def two_sum(lst, total=2020, start_index=0, end_index=None):
  so_far = set()
  for i in range(start_index, end_index or len(lst)):
    entry = lst[i]
    needed = total - entry
    if needed in so_far:
      return (needed, entry)
    else:
      so_far.add(entry)

def three_sum(lst):
  for i in range(len(lst)):
    curr = lst[i]
    needed = 2020 - curr
    valid = two_sum(lst, needed, i + 1)

    if valid:
      return (curr, valid[0], valid[1])


def get_input_list():
  input = open('1_input.txt', 'r')
  numbers = []
  for line in input:
    numbers.append(int(line.strip('\n')))
  return numbers


def part_1():
  one, two = two_sum(get_input_list())
  return one * two

def part_2():
  one, two, three = three_sum(get_input_list())
  return one * two * three