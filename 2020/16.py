def generate_checker(line):
  field, ranges = line.strip().split(': ')
  ranges_str = ranges.strip().split(' or ')
  ranges = []
  for r in ranges_str:
    start, end = r.split('-')
    ranges.append(range(int(start), int(end) + 1))

  return (field, lambda n: any([n in rng for rng in ranges]))

def read_ticket(line):
  return [int(n) for n in line.strip().split(',')]

def parse_input():
  input = open('16_input.txt', 'r')

  rules_by_field = {}
  nearby_tickets = []
  curr_state = 0
  for line in input:
    if line == '\n':
      curr_state += 1
      continue
    if curr_state == 0: # rules
      field, checker = generate_checker(line)
      rules_by_field[field] = checker
    elif curr_state == 1: # your ticket
      if line.strip() == 'your ticket:':
        continue
      your_ticket = read_ticket(line)
    else:
      if line.strip() == 'nearby tickets:':
        continue
      nearby_tickets.append(read_ticket(line))

  return rules_by_field, your_ticket, nearby_tickets

def part_1():
  rules_by_field, _, nearby_tickets = parse_input()
  check_satisfy_some = lambda n: any([check(n) for check in rules_by_field.values()])
  error_rate = 0
  for ticket in nearby_tickets:
    for val in ticket:
      if not check_satisfy_some(val):
        error_rate += val
  return error_rate

def part_2():
  rules_by_field, your_ticket, nearby_tickets = parse_input()

  # discard invalid nearby tickets
  check_satisfy_some = lambda n: any([check(n) for check in rules_by_field.values()])
  for ticket in nearby_tickets[:]:
    if not all([check_satisfy_some(val) for val in ticket]):
      nearby_tickets.remove(ticket)

  # narrow down valid fields for each index.
  fields_per_idx = {i:list(rules_by_field.keys()) for i in range(len(ticket))}

  for ticket in nearby_tickets:
    for i, value in enumerate(ticket):
      fields_to_check = fields_per_idx[i]
      for field in fields_to_check[:]:
        if not rules_by_field[field](value):
          fields_to_check.remove(field)

  # Do the sudoku constraints thing
  finalized = {} # field -> index
  while fields_per_idx:
    for i in list(fields_per_idx):
      fields = fields_per_idx[i]
      if len(fields) == 1:
        finalized[fields[0]] = i
        del fields_per_idx[i]
      else:
        fields_per_idx[i] = list(filter(lambda f: f not in finalized.keys(), fields))

  result = 1
  for field in finalized.keys():
    if 'departure' in field:
      result *= your_ticket[finalized[field]]
