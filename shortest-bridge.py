"""
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Input: A = [[0,1],[1,0]]
Output: 1

"""

def shortestbridge(islands):
  """
  Method: BFS
  
  first mark first island:
  - find all 1's of the first island, mark them as -1 visited
  - find all possible move to 0's, as 0's as visited, add them into a queue and it's dist
  
  - iterative from the queue, find all possible move
  from 0 coordinate and its distance to find second island which 1 that has not been marked
  
  -runtime O(NM), we visited every cell with size NxM only once
  -space O(NM), we could store all the coordinates up to NxM cell
  """ 
  rows = len(islands)
  cols = len(islands[0])
  deq = collections.deque()
  flag = False
  for r in range(rows):
    for c in range(cols):
      if islands[r][c] == 1:
        dfs(islands, rows, cols, r, c, deq)
        flag = True
        break
    if flag:
      break

  while deq:
    r, c, distance = deq.popleft()
    for x,y in [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]:
      if 0 <= x < rows and 0 <= y < cols and islands[x][y] != -1:
        if islands[x][y] == 1:
          return distance
        elif islands[x][y] == 0:
          islands[x][y] = -1
          deq.append((x, y, distance + 1))

  return 0
  
def dfs(islands, rows, cols, r, c, deq):

  if r < 0 or c < 0 or r >= rows or c >= cols or islands[r][c] == -1:
    return 

  if islands[r][c] == 1:
    island[r][c] = -1
    for x,y in [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]:
      dfs(islands, rows, cols, x, y, deq)
  elif islands[r][c] == 0:
    island[r][c] = -1
    deq.appendleft((r, c, 1))

