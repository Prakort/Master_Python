def Solution():
  def wordLadder(self, begin, end, wordList):
    
    parents = defaultdict(set)
    given = set(wordList)

    #using the child to parent to map the source and dist

    level = {begin}
    while level: 
      nextLevel = defaultdict(set)
      for word in level:
        for i in range(len(word)):
          for c in 'qwertyuiopasdfghjklzxcvbnm':
            src = word[:i] + c + word[i+1:]

            if src in given and src not in parents:
              nextLevel[src].add(word)

      level = nextLevel 
      parents.update(nextLevel)
    # up to n
    # 
    res = [[end]]
    # find all paths backward to the beginword
    while res and res[0][0] != begin:
      temp = []
      for i in res: 
        for p in parents[i[0]]:
          # combine both cur and new list by keeping the new word at the start
          # it could update the and check for new word parent node next outter loop
          temp.append([p] + i)

      res = temp

    return res



   






