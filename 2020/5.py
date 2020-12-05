def get_seat_id(bp):
  lower, upper = 0, 127
  for r in bp[:7]:
    if r == 'F':
      upper = (lower + upper - 1) // 2
    else:
      lower = (lower + upper + 1) // 2
  row = lower # At this point, lower == upper == row

  lower, upper = 0, 7
  for c in bp[7:]:
    if c == 'L':
      upper = (lower + upper - 1) // 2
    else:
      lower = (lower + upper + 1) // 2
  column = lower # lower == upper == row

  return row * 8 + column

def part_1():
  input = open('5_input.txt', 'r')
  return max([get_seat_id(line.strip()) for line in input])

def part_2():
  input = open('5_input.txt', 'r')

  min_id, max_id, sum_ids = 1023, 0, 0
  for line in input:
    seat_id = get_seat_id(line.strip())
    min_id = min(seat_id, min_id)
    max_id = max(seat_id, max_id)
    sum_ids += seat_id

  expected_sum = (max_id - min_id + 1) * (max_id + min_id) / 2
  return expected_sum - sum_ids
