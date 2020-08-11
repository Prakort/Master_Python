def solution(being, end, wordList):
  # find the min step of sequence to tranform being to end word 
  # one char at a time
  # from the wordList

  # since we only change 1 char at a time, we have to try all possible char a -> z 
  # for every index of current word to see if the new word exists in the wordlist
  # car -> cat -> dat count as 2

  # 26x(word length) x given words
  # => MxN same space
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

