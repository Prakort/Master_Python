def solution(S):
  # find the last index for all char
  index = defaultdict(int)
  for i,c in enumerate(S):
    index[c] = i 

  res = []
  start = end = 0
  for i in range(len(S)):
    end = max(end, index[S[i]]) # a b       b a b
    if end == i: # if there is no any char in the partition has larger index of the last occurence
      res.append(end - start + 1)
      start = end + 1

  return res

