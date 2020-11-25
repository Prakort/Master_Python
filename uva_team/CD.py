""" 
Prakort Lean
104932087
"""

n,m = [int(x) for x in input().split(" ")]

counter = 0
s = set()
while True:
  try:
    line = input()
    if line == "0 0":
      break 
    s.add(line)
  except:
    pass
print(n+m - len(s))
