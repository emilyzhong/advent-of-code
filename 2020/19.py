import re

def parse_input():
  input = open('19_input.txt', 'r')
  rules = {}
  for line in input:
    if line == '\n':
      break
    key, val = [s.strip() for s in line.strip().split(':')]

    if '|' in val:
      val = val.split('|')
      val = [[int(n) for n in group.strip().split(' ')] for group in val]
    elif '"' in val:
      val = val.replace('"', '')
    else:
      val = [int(n) for n in val.strip().split(' ')]
    rules[int(key)] = val

  messages = [line.strip() for line in input]
  return rules, messages

def rule_to_regex(rule, rules, rule_num=None):
  if not isinstance(rule, list):
    return f'({rule})'
  elif isinstance(rule[0], list):
    return f'({rule_to_regex(rule[0], rules, rule_num)}|{rule_to_regex(rule[1], rules, rule_num)})'
  else:
    if rule_num in rule:
      repeat = rule.index(rule_num)
      beg, end = rule[:repeat], rule[repeat+1:]
      if not end:
        regexes = [rule_to_regex(rules[i], rules, i) for i in beg]
        regexes[-1] += '+'
      else:
        # hacky hacky
        return rule_to_regex([
          beg + end,
          beg * 2 + end * 2,
          beg * 3 + end * 3,
          beg * 4 + end * 4,
          beg * 5 + end * 5,
          beg * 6 + end * 6,
          beg * 7 + end * 7,
          beg * 8 + end * 8,
          beg * 9 + end * 9,
        ], rules)
    else:
      regexes = [rule_to_regex(rules[i], rules, i) for i in rule]
    return f'({"".join(regexes)})'

def part_1():
  rules, messages = parse_input()
  pattern = re.compile(f'^{rule_to_regex(rules[0], rules)}$')
  return sum([bool(pattern.match(m)) for m in messages])

def part_2():
  rules, messages = parse_input()
  rules[8] = [[42], [42, 8]]
  rules[11] = [[42, 31], [42, 11, 31]]
  pattern = re.compile(f'^{rule_to_regex(rules[0], rules, 0)}$')
  for m in messages:
    if pattern.match(m):
      print(m)
  return sum([bool(pattern.match(m)) for m in messages])

print(part_1())
print(part_2())