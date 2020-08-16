def solution(paragraph, banned):
  lowerCase = []
  for c in paragraph:
    if c.isalnum():
      lowerCase.append(c.lower())
    else:
      lowerCase.append(" ")
  words = ''.join(lowerCase).split()
  
  map = defaultdict(int)

  for word in words:
    if word not in banned:
      map[word] += 1
    
  res = [ (map[w], w) for w in map]
  res = res.sort(key = lambda x: x[0], reverse = True)

  return res[0][1]
