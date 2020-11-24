

def DFS(word, index, current):
  if index == len(word):
    print(current)
    return 
  for i in range(len(current)+1):
    DFS(word, index+1, current[:i] + word[index] + current[i:])

flag = 0
while(True):
  try:
    word = input()

    DFS(word, 0, "")
    if(flag):
      print("\n")
    flag = 1
  except:
    pass
