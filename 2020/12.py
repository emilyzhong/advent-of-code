import math

def part_1():
  curr_dir = 0 # degrees
  curr_x = 0
  curr_y = 0
  input = open('12_input.txt', 'r')
  for line in input:
    line = line.strip()
    dir, amt = line[0], int(line[1:])
    if dir == 'N':
      curr_y += amt
    elif dir == 'S':
      curr_y -= amt
    elif dir == 'E':
      curr_x += amt
    elif dir == 'W':
      curr_x -= amt
    elif dir == 'F':
      x_mult = math.cos(math.radians(curr_dir))
      y_mult = math.sin(math.radians(curr_dir))
      curr_x += amt * x_mult
      curr_y += amt * y_mult
    elif dir == 'L':
      curr_dir = (curr_dir + amt) % 360
    elif dir == 'R':
      curr_dir = (curr_dir - amt) % 360
  return abs(curr_x) + abs(curr_y)

def part_2():
  waypoint_x = 10
  waypoint_y = 1

  curr_x = 0
  curr_y = 0

  input = open('12_input.txt', 'r')
  for line in input:
    line = line.strip()
    dir, amt = line[0], int(line[1:])
    if dir == 'N':
      waypoint_y += amt
    elif dir == 'S':
      waypoint_y -= amt
    elif dir == 'E':
      waypoint_x += amt
    elif dir == 'W':
      waypoint_x -= amt
    elif dir == 'F':
      curr_x += amt * waypoint_x
      curr_y += amt * waypoint_y
    elif dir == 'L':
      mag = math.sqrt(waypoint_x ** 2 + waypoint_y ** 2)
      theta = math.atan2(waypoint_y, waypoint_x)
      theta += math.radians(amt)

      waypoint_x = mag * math.cos(theta)
      waypoint_y = mag * math.sin(theta)
    elif dir == 'R':
      mag = math.sqrt(waypoint_x ** 2 + waypoint_y ** 2)
      theta = math.atan2(waypoint_y, waypoint_x)
      theta -= math.radians(amt)

      waypoint_x = mag * math.cos(theta)
      waypoint_y = mag * math.sin(theta)
  return abs(curr_x) + abs(curr_y)

print(part_2())

