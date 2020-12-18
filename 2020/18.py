def find_closing_paren(line):
  num_opened = 1
  for i in range(1, len(line)):
    if line[i] == ')':
      num_opened -= 1
    elif line[i] == '(':
      num_opened += 1
    if num_opened == 0:
      return i

def solve_equation_2(line):
  prev_val = 0
  prev_operator = '+'
  while line:
    token = line[0]
    next_val = None
    if token == '(':
      closing = find_closing_paren(line)
      next_val = solve_equation(line[1:closing])
      line = line[closing + 1:]
    elif token == '+':
      prev_operator = token
      line = line[1:]
    elif token == '*':
      prev_operator = token
      next_val = solve_equation(line[1:])
      line = ''
    elif token in [' ', '\n']:
      line = line[1:]
    else:
      next_val = int(token)
      line = line[1:]

    if next_val is not None:
      if prev_operator == '+':
        prev_val += next_val
      else:
        prev_val *= next_val

  return prev_val

def solve_equation_1(line):
  prev_val = 0
  prev_operator = '+'
  while line:
    token = line[0]
    next_val = None
    if token == '(':
      closing = find_closing_paren(line)
      next_val = solve_equation(line[1:closing])
      line = line[closing + 1:]
    elif token in ['*', '+']:
      prev_operator = token
      line = line[1:]
    elif token in [' ', '\n']:
      line = line[1:]
    else:
      next_val = int(token)
      line = line[1:]

    if next_val is not None:
      if prev_operator == '+':
        prev_val += next_val
      else:
        prev_val *= next_val
  return prev_val

def part_1():
  return sum([solve_equation_1(line) for line in open('18_input.txt', 'r')])

def part_2():
  return sum([solve_equation_2(line) for line in open('18_input.txt', 'r')])
