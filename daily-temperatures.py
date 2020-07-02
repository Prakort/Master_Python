def solution(T):
  """
  [73,74]
  [1, 0]
  at index i = 0 have to wait 1 day
  at index i = 1 is the end
  [73, 74, 75]
  [1, 1, 0]

  we could find the # of days but subtracting the index of the warmer day - previous colder day

  we could process one day by a time in a stack to keep track which has been looked up yet

  if we find a warmer day than the top index of the stack, then we find the # days that index has to wait, and we keep popping the stack until it is stack or the day in the stack is warmer that current index
  """

  previous_days = []
  res = [0] * len(T)

  for i in range(len(T)):
    while previous_days and T[i] > T[previous_days[-1]]:
      colder_day = previous_days.pop()
      res[colder_day] = i - colder_day
      
    previous_days.append(i)
    
  return res
