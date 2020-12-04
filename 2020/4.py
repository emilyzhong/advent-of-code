import re

# Helper validator functions for part 2 >:(
def validate_byr(yr):
  yr = int(yr)
  return yr >= 1920 and yr <= 2002

def validate_iyr(yr):
  yr = int(yr)
  return yr >= 2010 and yr <= 2020

def validate_eyr(yr):
  yr = int(yr)
  return yr >= 2020 and yr <= 2030

def validate_hgt(ht):
  matches = re.match(r'^([0-9]+)(cm|in)$', ht)
  if (matches is None):
    return False
  val, units = matches.groups()
  val = int(val)
  return (units == 'in' and val >= 59 and val <= 76) or (
    units == 'cm' and val >= 150 and val <= 193)

def validate_hcl(color):
  return re.match(r'^#[0-9a-f]{6}$', color)

def validate_ecl(color):
  return color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validate_pid(pid):
  return re.match(r'^[0-9]{9}$', pid)

def validate_cid(cid):
  return True

field_validator = {
  'byr': validate_byr,
  'iyr': validate_iyr,
  'eyr': validate_eyr,
  'hgt': validate_hgt,
  'hcl': validate_hcl,
  'ecl': validate_ecl,
  'pid': validate_pid,
  'cid': validate_cid
}

required_keys = set(field_validator.keys()) - {'cid'}

def solve(validator):
  input = open('4_input.txt', 'r')
  passport = set()
  num_valid = 0

  for line in input:
    if len(line) == 1: # only new-line
      if len(required_keys.difference(passport)) == 0:
        num_valid += 1
      passport = set()
    else:
      tokens = re.split(r':|\s', line.strip())
      for i in range(0, len(tokens), 2):
        key = tokens[i]
        value = tokens[i + 1]
        if validator(key, value):
          passport.add(key)

  # Catch final passport entry
  if len(required_keys.difference(passport)) == 0:
    num_valid += 1

  return num_valid

def part_1():
  validator = lambda key, value: True
  return solve(validator)

def part_2():
  validator = lambda key, value: field_validator[key](value)
  return solve(validator)
