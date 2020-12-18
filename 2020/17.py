def neighbor_diffs(dim):
  diffs = [-1, 0, 1]
  neighbors = [()]
  for _ in range(dim):
    temp_neighbors = []
    for diff in diffs:
      temp_neighbors += [tuple(list(n) + [diff]) for n in neighbors]
    neighbors = temp_neighbors

  zeros = tuple([0 for _ in range(dim)])
  neighbors.remove(zeros)
  return neighbors

def get_neighbors(coord):
  dim = len(coord)
  diffs = neighbor_diffs(dim)
  neighbors = []

  for diff in diffs:
    neighbors.append(tuple([coord[i] + diff[i] for i in range(dim)]))
  return neighbors

def solve(dim):
  active = set() # set of x, y, z[, w]
  input = open('17_input.txt', 'r')
  y = 0
  for line in input:
    for i in range(len(line)):
      if line[i] == '#':
        active.add(tuple([i, y] + [0 for _ in range(dim - 2)]))
    y += 1

  for _ in range(6):
    temp = {} # xyz[w] coordinate -> number of active neighbors
    for coord in active:
      if coord not in temp:
        temp[coord] = 0
      neighbors = get_neighbors(coord)
      for neighbor in neighbors:
        if neighbor not in temp:
          temp[neighbor] = 0
        temp[neighbor] += 1

    for coord, num_neighbors in temp.items():
      if coord in active and (num_neighbors not in [2, 3]):
        active.remove(coord)
      elif coord not in active and num_neighbors == 3:
        active.add(coord)
  return len(active)

part_1 = lambda: solve(3)
part_2 = lambda: solve(4)
