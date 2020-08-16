def solution(image, sr, sc, newColor):
  # we want to find the start cell color:
  # runnime: O(mxn)
  startColor = image[sr][sc]
  rows = len(image)
  cols = len(image[0])

  if startColor == newColor:
    return image 

  dfs(image, rows, cols, sr, sc, newColor, startColor)

  return image

def dfs(image, rows, cols, r, c, newColor, startColor):
  if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != startColor:
    return

  image[r][c] = newColor 
  for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
    dfs(image, rows, cols, i, j, newColor, startColor)



  
