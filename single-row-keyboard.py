def solution(keyboard, word):
  w = len(word)
  if not w:
    return 0
  
  hm = {}
  for i in range(len(keyboard)):
    hm[keyboard[i]] = i
    
  counter = hm[word[0]]
  for i in range(1, w):
    counter += abs(hm[word[i-1]] - hm[word[i]])
    
  return counter
