def solution(words):
  """
  Input:
  [
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
  ]

  Output: "wertf"
  Goal is to find relationship between each node

  "wrt" , "wrf"  => w is before r is before t is before f 

  "wrf", "er" => w is before e is before r

  we could see the pattern between first char of the two words
  and the first different char. 

  we could build graph as start node points to distination
  -start is the before char
  -distination is the after char
  -distination can have mulitple start nodes
  e.g.
  "rt"
  "yt"
  r -> y
  r -> t 
  y -> t   
  r -> y -> t, we will use hashmap to count how many time we find distination from start
  that count is called Degree of a vortex
  that means the very first char has Degree Zero
  we will use topological sort to find order
  """
  #hashmap <char, set()>
  hm = {}
  #hashmap counter of Degree of each distination
  #Degree of very first nodes is zero
  indegree = Counter({c: 0 for word in words for c in word})
  
  #prepare the graph, add <start, set(distination)>
  for i in range(len(words)):
    for ch in words[i]:
      # add empty list of distination for start vortex
      hm[ch] = set()

  #build graph
  for i in range(1, len(words)):
    w1 = words[i-1]
    w2 = words[i]
    for j in range(len(w1)):
      # if there is no diff char between  within min(len(w1),len(w2)) if len(w1) > len(w1)
      # return '' meaning wrong order
      # e.g, wrt, wr ==> it should be wr, wrt (failed return '' right away)
      # e.g, wrt, er ==> first index, we consinder w -> e (YES, break out of loop) w is the start, e is the distination
      # using this condition instead of len(w1) > len(w2)
      # allow us to get all possible orders even the lengths are not the same
      if j == len(w2):
        return ''
      if w1[j] != w2[j]:
        start = w1[j]
        dist = w2[j]
        # check if distination is already added in map of start
        if dist not in hm[start]:
          # add distination into the set
          hm[start].add(dist)
          # we found distination, increment its Degree
          indegree[dist] += 1
        # break after finding the first diff between w1 and w2
        break

  # --- end of building graph --- #
  # deque, deck
  deck = deque()
  # result
  res = ""
  # find the zero degree node
  # they are the first char
  for ch in hm.keys():
    # if the degree is zero we add into the deck
    # in this case, they are zero because they are not distination node
    # we will see when degree of distination node is zero
    if indegree[ch] == 0:
      deck.appendleft(ch)
      res += ch

  
  # iterate the deck and find its distination
  while deck:
    start = deck.popleft()
    # find all possible distination of a start node
    for dist in hm[start]:
      # decrement its degree
      indegree[dist] -= 1
      # if distination degree is zero
      # that means, its order is after the start node above
      # add to the res
      if indegree[dist] == 0:
        res += dist 
        # of course we have to add dist into the deck
        # dist in the deck will be start to find its next distination node
        deck.append(dist)

  # if there is a loop,
  # answer should be char in hashmap
  # but if there is a loop, counter will never be zero
  # then length of res is less than hashmap
  return res if len(res) == len(hm) else ""
