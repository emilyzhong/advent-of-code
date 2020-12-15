def solve(num_iter):
  numbers = [20,9,11,0,1,2]
  last_said = {} # map # -> last two times it has been said.
  for i in range(num_iter):
    if i < len(numbers):
      last_said[numbers[i]] = [i]
      last_number = numbers[i]
      continue

    # get new number for this turn
    indices = last_said[last_number]
    if len(indices) == 1:
      last_number = 0
    else:
      last_number = indices[-1] - indices[-2]

    # update last_said for new number this turn
    if last_number in last_said:
      last_said[last_number] = [last_said[last_number][-1]] + [i]
    else:
      last_said[last_number] = [i]

  return last_number

part_1 = lambda: solve(2020)
part_2 = lambda: solve(30000000)
