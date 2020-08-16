def solution(grid):
  # question one or more rotten oranges?
  # could modify the input list?
  # let find all the bad orange
  rows = len(grid)
  cols = len(grid[0])
  res = 0
  fresh_oranges = 0
  deck = deque()
  for i in range(rows):
    for j in range(cols):
      if grid[i][j] == 2:
        deck.append((i,j,0))
        grid[i][j] = -2
      elif grid[i][j] == 1:
        fresh_oranges = fresh_oranges + 1

  while deck:
    r, c, minute = deck.pop()
    for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
      if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
        fresh_oranges = fresh_oranges - 1
        # add to the start of the list since it's BFS
        deck.appendleft((i,j, minute + 1))
        grid[i][j] = -2

  return 0 if fresh_oranges == 0 else res

