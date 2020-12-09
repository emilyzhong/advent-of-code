# from 1.py!!!
def two_sum(lst, total, start_index=0, end_index=None):
  so_far = set()
  for i in range(start_index, end_index or len(lst)):
    entry = lst[i]
    needed = total - entry
    if needed in so_far:
      return (needed, entry)
    else:
      so_far.add(entry)

def input():
  input = open('9_input.txt', 'r')
  return [int(line.strip()) for line in input]

def part_1(lst=None):
  lst = lst or input()
  for i in range(0, len(lst)):
    if not two_sum(lst, total=lst[i + 26], start_index=i, end_index=i + 26):
      return lst[i + 26]

def part_2():
  lst = input()
  n = part_1(lst)
  start = 0
  end = 1
  tmp = 0
  while end <= len(lst) and start < len(lst):
    tmp += lst[end - 1]
    while tmp > n:
      tmp -= lst[start]
      start += 1
    if tmp == n:
      rng = lst[start:end]
      return min(rng) + max(rng)
    else:
      end += 1
