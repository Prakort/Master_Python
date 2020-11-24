"""
Prakort Lean
104932087
"""

hm = {}
for i in range(26):
  if i >= 21:
    hm[i] = 2
  elif i >= 16:
    hm[i] = 3 
  elif i >= 11:
    hm[i] = 4 
  elif i >= 1:
    hm[i] = 5
  
line = input()
legend = False 
wins = 0
ranks = 25 
stars = 0

for c in line:
  if c == 'W':
    wins += 1 
    if wins >= 3 and ranks >= 6:
      stars +=1 
      if hm[ranks]+ 1 == stars:
        ranks -=1 
        stars = 1
    
    stars += 1
    if hm[ranks] + 1 == stars:
      ranks -= 1
      stars = 1
    if ranks == 0:
      legend = True
  else:
    wins = 0
    if ranks <= 20:
      stars -=1 
    if stars == -1 :
      if ranks == 20:
        stars = 0
      else:
        ranks +=1
        stars = hm[ranks] - 1

if not legend:
  print(ranks)
else:
  print("Legend")



