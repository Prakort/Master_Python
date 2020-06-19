def solution(tasks):
  """
  Input: tasks = ["A","A","A","B","B","B"], n = 2
  Output: 8
  Explanation: 
  A -> B -> idle -> A -> B -> idle -> A -> B
  There is at least 2 units of time between any two same tasks.

  - Notice that we must complete the most occurrence task first each interval
  - at least n interval between starting the same task

  """

  counter = Counter(tasks)
  heap, time = [], 0

  for value in counter:
    # convert min heap to max heap using negation
    heapq.heapush(heap, -value)

  
  # iterate until no more task in the heap
  while heap:
    # keep track of the tasks been used in the interval n
    current = []
    # iterate from 1 to N + 1 times why? we want to count "A" + n(tasks) -> "A", each iteration is N+1 not N,
    for i in range(n+1):
      # check if heap is not empty
      if heap:
        # pop the most occurrence tasks
        value = heapq.heappop(heap)
        # if the number of tasks is not zero, value > 1 ==> value < -1 since value is negative val
        if value < -1 :
          # add into the current list to keep track which task has been done
          # + 1 to decrement the value
          current.append(value + 1)
        
        # since we keep popping the heap we have to check if heep is empty
        if not heap and not current:
          # return count + 1, since this is still in the one iteration from 1 to N+1
          return time + 1
      time += 1
    # update the count of the tasks from the list
    for task in current:
      heapq.heapush(heap, task)


  return time
