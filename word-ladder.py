def solution(being, end, wordList):
  # find the min step of sequence to tranform being to end word 
  # one char at a time
  # from the wordList

  # since we only change 1 char at a time, we have to try all possible char a -> z 
  # for every index of current word to see if the new word exists in the wordlist
  # car -> cat -> dat count as 2

  # 26x(word length) x given words
  # => MxN same space
  # time: O(NxM) N len(wordlist), M = len(word) O(NxM)
  # space: O(N) len(wordlist)
  q = deque()
  q.append((being, 1))
  given = set(wordList)
  while q:
    cur, level = q.popleft()
    if cur == end:
      return level
    for i in range(len(cur)):
      temp = list(cur)
      for c in range(26):
        temp[i] = chr(c + ord('a'))
        new_word = ''.join(temp)

        if new_word in given and new_word != cur:
          q.append((new_word, level + 1))
          given.remove(new_word)

  return 0


def bidirectional(beginWord, endWord, wordList):
    # hit -> hot -> dot -> dog -> cog 
    #            -> lot -> log -> cog  
    if endWord not in wordList:
        return 0
    # wordList.append(beginWord)
    qFront = deque([(beginWord, 1)])
    qEnd = deque([(endWord, 1)])
    
    seenFront = set([beginWord])
    seenEnd = set([endWord])
    
    parentFront = defaultdict(str)
    parentEnd = defaultdict(str)
    
    parentFront[beginWord] = beginWord
    parentEnd[endWord] = endWord
    
    while qFront and qEnd:
        curFront, levelFront = qFront.popleft()
        curEnd, levelEnd = qEnd.popleft()
        
        intersect = seenFront.intersection(seenEnd)
        if len(intersect) != 0:
            word = intersect.pop()
            counterToFront = 1
            counterToEnd = 1
            wordFront = word
            wordEnd = word
            while parentFront[wordFront] != wordFront:
                wordFront = parentFront[wordFront]
                counterToFront += 1
            while parentEnd[wordEnd] != wordEnd:
                wordEnd = parentEnd[wordEnd]
                counterToEnd += 1
        #front < -- middle - > end
            print("hi", word)
            return counterToFront + counterToEnd - 1 
        for i in range(len(curFront)):
            for j in 'asdfghjklqwertyuiopzxcvbnm':
                newWord = curFront[:i] + j + curFront[i+1:]

                if newWord == endWord:
                    return levelFront + 1
                if newWord in wordList and newWord not in seenFront:
                    qFront.append((newWord, levelFront + 1))
                    parentFront[newWord] = curFront
                    seenFront.add(newWord)
                    
        for i in range(len(curEnd)):
            for j in 'asdfghjklqwertyuiopzxcvbnm':
                newWord = curEnd[:i] + j + curEnd[i+1:]
                if newWord == beginWord:
                    return levelEnd + 1
                if newWord in wordList and newWord not in seenEnd:
                    qEnd.append((newWord, levelEnd + 1))
                    parentEnd[newWord]= curEnd
                    seenEnd.add(newWord)
                    
    return 0
            
                
        
