def solution(words, order):

  """
  we have order, show that words are sorted based on that order
  we will compare two words and compare each char at same index, check their indexes in the order
  """

  for i in range(len(words)-1):
    w1 = words[i]
    w2 = words[i+1]
    # w1 should be always shorter
    for j in range(w1):
      # means w1 is longer
      if j == len(w1):
        return False 
      if order.index(w1[j]) < order.index(w2[j]):
        break
      if order.index(w1[j]) > order.index(w2[j]):
        return False 

  return True
