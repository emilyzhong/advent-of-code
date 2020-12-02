def part_1_validator(low, high, letter, password):
  num_letter = sum([int(c == letter) for c in password])
  return num_letter >= low and num_letter <= high

def part_2_validator(low, high, letter, password):
  low_index = low - 1
  high_index = high - 1
  return (password[low_index] == letter) is not (password[high_index] == letter)

def solve(is_valid_password):
  num_valid_passwords = 0
  input = open('2_input.txt', 'r')
  for line in input:
    tokens = line.split()

    rng = tokens[0].split('-')
    low, high = int(rng[0]), int(rng[1])

    char = tokens[1][0] # drop the colon
    password = tokens[2]

    num_valid_passwords += int(is_valid_password(low, high, char, password))
  return num_valid_passwords

def part_1():
  return solve(part_1_validator)

def part_2():
  return solve(part_2_validator)
