"""
Prakort Lean
104932087
"""

i = 1
while True:
  try:
    word = str(input())
    search = str(input()) 
    print(word, search, i)
    if(word is None or search is None):
      print("{}. Blank!".format(i))
      continue
    print("{}. {}".format(i, word))
    i +=1

  except:
    break
delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
