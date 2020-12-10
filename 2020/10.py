def input():
  lst = [int(line.strip()) for line in open('10_input.txt', 'r')]
  lst.sort()
  lst.insert(0, 0) # outlet
  lst.append(lst[-1] + 3) # device
  return lst

def part_1():
  lst = input()
  prev, ones, threes = 0, 0, 0
  for n in lst:
    ones += (n - prev == 1)
    threes += (n - prev == 3)
    prev = n
  return ones * threes

def part_2():
  lst = input()
  dp = [0 for _ in lst]
  for i in range(1, len(lst)):
    j = i - 1
    total = 0
    while lst[i] - lst[j] <= 3 and j >= 0:
      total += dp[j]
      j -= 1
    dp[i] = total
  return dp[-1]
