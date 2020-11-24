import collections

"""
Prakort Lean
104903287
"""

n = int(input())

for i in range(n):
  flag = 0
  op = input()
  num = int(input())
  line = input()
  # print(op, num, line)
  line = collections.deque(line[1:-1].split(","))
  for c in op:

    if flag == 1:
      break
    if c == "R":
      if num != 0:
        line.reverse()
      else:
       
        flag = 1
        break 
    elif c == "D":
  
      if num != 0:
        num -=1
        line.popleft()
      else:
        flag = 1
        break

  if flag == 0:
    print("[" + ",".join(list(line)) + "]")
  else:
    print("error")
  # print(line)
