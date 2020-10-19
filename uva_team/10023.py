def solution(x):
  print("input is: ", x)
  low = 1
  hi = x // 2

  while low <= hi:
    mid = (hi + low) // 2
    n = mid * mid 
    if n > x :
      low = mid + 1
    elif n < x :
      hi = mid - 1
    else :
      return mid 

  return "Big no no"

print("answer of 7206604678144 is: ", solution(7206604678144))
