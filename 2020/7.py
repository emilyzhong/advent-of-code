def parse_rule(line):
  remove_bag_substr = lambda s: s.replace('bags', '').replace('bag', '').strip()
  line = line.strip().split('contain')
  outer_bag = remove_bag_substr(line[0])

  inner_bags = line[-1].replace('.', '').split(',')
  inner_bags = filter(lambda b: b != 'no other', [remove_bag_substr(bag) for bag in inner_bags])
  inner_bags = [(int(bag[0]), bag[2:]) for bag in inner_bags]

  return outer_bag, inner_bags

def part_1():
  input = open('7_input.txt', 'r')
  bag_to_parents = {} # bag color -> set of bag colors than can hold it
  for line in input:
    outer_bag, inner_bags = parse_rule(line)

    for _, bag in inner_bags:
      if bag not in bag_to_parents:
        bag_to_parents[bag] = set()
      bag_to_parents[bag].add(outer_bag)

  # Run tree traversal
  queue = ['shiny gold']
  can_hold = set()
  while queue:
    curr = queue.pop()
    if not curr in bag_to_parents:
      continue

    parents = bag_to_parents[curr]
    for parent in parents:
      if parent not in can_hold:
        queue.append(parent)
  return len(can_hold) - 1

def part_2():
  input = open('7_input.txt', 'r')
  bag_to_children = {} # bag color -> set of (number, bag color) that it must hold
  for line in input:
    outer_bag, inner_bags = parse_rule(line)

    if outer_bag not in bag_to_children:
      bag_to_children[outer_bag] = set()
    bag_to_children[outer_bag] ^= set(inner_bags)

  # Run tree traversal
  queue = [(1, 'shiny gold')]
  total = 0
  while queue:
    count, color = queue.pop()
    total += count
    if not color in bag_to_children:
      continue

    children = bag_to_children[color]
    for child_count, child in children:
      queue.append((child_count * count, child))
  return total - 1
