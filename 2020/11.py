def part_1_visible_seats(i, j, state):
  seats = []
  for delt_i in range(-1, 2):
    for delt_j in range(-1, 2):
      seat_i = i + delt_i
      seat_j = j + delt_j
      if (delt_i == 0 and delt_j == 0) or \
        seat_i < 0 or seat_j < 0 or \
        seat_i >= len(state) or seat_j >= len(state[0]):
        continue
      seats.append(state[seat_i][seat_j])
  return seats

def part_2_visible_seats(i, j, state):
  seats = []
  def check(check_i, check_j):
    if state[check_i][check_j] != '.' and not (check_i == i and check_j == j):
      seats.append(state[check_i][check_j])
      return True

  # left
  for seat_j in range(j, -1, -1):
    if check(i, seat_j):
      break
  # right
  for seat_j in range(j, len(state[0])):
    if check(i, seat_j):
      break
  # up
  for seat_i in range(i, -1, -1):
    if check(seat_i, j):
      break
  # down
  for seat_i in range(i, len(state)):
    if check(seat_i, j):
      break

  # upper left
  seat_i, seat_j = i, j
  while seat_i >= 0 and seat_j >= 0:
    if check(seat_i, seat_j):
      break
    seat_i -= 1
    seat_j -= 1

  # upper right
  seat_i, seat_j = i, j
  while seat_i >= 0 and seat_j < len(state[0]):
    if check(seat_i, seat_j):
      break
    seat_i -= 1
    seat_j += 1

  # lower right
  seat_i, seat_j = i, j
  while seat_i < len(state) and seat_j < len(state[0]):
    if check(seat_i, seat_j):
      break
    seat_i += 1
    seat_j += 1

  # lower left
  seat_i, seat_j = i, j
  while seat_i < len(state) and seat_j >= 0:
    if check(seat_i, seat_j):
      break
    seat_i += 1
    seat_j -= 1

  return seats

def solve(get_visible_seats, free_up_threshold=4):
  input = open('11_input.txt', 'r')
  state = [list(line.strip()) for line in input]
  has_changed = True
  while has_changed:
    has_changed = False
    next_state = []
    for i in range(len(state)):
      new_row = []
      row = state[i]
      for j in range(len(row)):
        seat = row[j]
        new_seat = seat
        if seat != '.':
          adjacent = get_visible_seats(i, j, state)
          if seat == "L":
            new_seat = "L" if "#" in adjacent else "#"
          elif seat == '#':
            new_seat = "L" if sum([s == '#' for s in adjacent]) >= free_up_threshold else "#"

        has_changed = has_changed or (new_seat != seat)
        new_row.append(new_seat)
      next_state.append(new_row)
    state = next_state

  # print(state)
  # print('\n'.join([''.join([str(cell) for cell in row]) for row in state]))
  return sum([sum([seat == '#' for seat in row]) for row in state])

def part_1():
  return solve(part_1_visible_seats, 4)

def part_2():
  return solve(part_2_visible_seats, 5)
