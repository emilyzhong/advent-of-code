def check_slope(delta_x = 3, delta_y = 1):
  input = open('3_input.txt', 'r')
  x_index = 0
  y_index = 0
  num_collisions = 0
  for line in input:
    curr_line = line.strip('\n')

    if y_index == 0:
      if curr_line[x_index] == "#":
        num_collisions += 1
      x_index = (x_index + delta_x) % len(curr_line)

    y_index = (y_index + 1) % delta_y

  return num_collisions

def part_1():
  return check_slope(3, 1)

def part_2():
  a = check_slope(1, 1)
  b = check_slope(3, 1)
  c = check_slope(5, 1)
  d = check_slope(7, 1)
  e = check_slope(1, 2)

  return a * b * c * d * e
