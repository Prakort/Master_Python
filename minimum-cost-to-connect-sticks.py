def solution(sticks):
  # we want to add X + Y as get the minimum cost
  # keep redoing it untill there is only one stick left 
  # we have to pick two smallest sticks and add them to together
  # and add the new stick into the list 
  # we need to reorder the list so we could get the two smallest sticks for the next operation

  # create a min-heap
  # it takes O(nlogn) to build a heap
  heap = []
  for stick in sticks:
    heapq.heappush(heap, stick)

  cost = 0
  # we want to leave 1 stick left in the list
  while len(heap) > 1:
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    newStick = x + y
    # update the cost
    cost += newStick
    # add the new stick back into the list
    # heap will heapify and sort the list
    heapq.heappush(heap, newStick)

  return cost

