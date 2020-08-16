def solution(products, searchWord):
  # we want to sort the products words first
  products.sort()
  res = []
  # iterate to find the prefix
  for i in range(len(searchWord)):
    prefix = searchWord[:i+1]
    j = 0 
    temp = []
    for word in products:
      if word.startswith(prefix):
        temp.append(word)
        j +=1 

      if j == 3:
        break

    res.append(temp)
  return res
