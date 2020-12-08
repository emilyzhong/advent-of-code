def parse_input():
  input = open('8_input.txt', 'r')
  program = []
  for line in input:
    instr, arg = line.strip().split()
    program.append((instr, int(arg)))
  return program

def run_instruction(instr, arg, curr_line, acc, backwards = False, is_modified = False):
  mult = -1 if backwards else 1
  if instr == 'acc':
    return curr_line + mult * 1, acc + arg
  elif (instr == 'nop' if is_modified else instr == 'jmp'):
    return curr_line + mult * arg, acc
  elif (instr == 'jmp' if is_modified else instr == 'nop'):
    return curr_line + mult * 1, acc
  return curr_line, acc

def part_1():
  program = parse_input()
  seen_lines = set()
  acc, curr_line = 0, 0
  while curr_line not in seen_lines:
    seen_lines.add(curr_line)
    instr, arg = program[curr_line]
    curr_line, acc = run_instruction(instr, arg, curr_line, acc)
  return acc

def part_2():
  program = parse_input()

  # line # -> array of parent lines, represented as tuples (line, was_modified)
  instruction_tree = [[] for _ in range(len(program))]
  last_lines = []
  for i in range(len(program)):
    instr, arg = program[i]
    modifiers = [False] if instr == 'acc' else [False, True]
    for is_modified in modifiers:
      next_line, _ = run_instruction(instr, arg, i, 0, is_modified=is_modified)
      if next_line >= len(program):
        last_lines.append((i, is_modified))
      else:
        instruction_tree[next_line].append((i, is_modified))

  # Run tree traversal from last_lines, with accumulator value stored
  last_lines = [(line[0], line[1], 0) for line in last_lines]
  seen_lines = set()
  while last_lines:
    line, is_modified, acc = last_lines.pop()
    instr, arg = program[line]

    # since the nop and jmp don't affect accumulated values, doesn't matter if line is modified
    _, new_acc = run_instruction(instr, arg, line, acc, backwards=True)
    if line == 0: # we can reach the last line from the start!
      return new_acc

    seen_lines.add((line, is_modified))
    instr, arg = program[line]

    for parent_line, parent_is_modified in instruction_tree[line]:
      next_is_modified = is_modified or parent_is_modified
      if is_modified and parent_is_modified or (parent_line, next_is_modified) in seen_lines:
        continue
      else:
        last_lines.append((parent_line, next_is_modified, new_acc))
