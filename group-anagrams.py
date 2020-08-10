def solution(strs):
  res = []
  groups = {}

  for word in strs:
    counter = Counter(word)

    k = tuple(counter)
    if k in groups:
      groups[k].append(word)
    else:
      group[k] = [word]

  return groups.values()
