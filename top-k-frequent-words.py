def solution(words):
  counter = collections.Counter(words)
  

  pairs = [(-counter[key],key) for key in counter]
  # heapq in python has special operation on turple which allow comparison
  # heapq heapify is a min heap, we add negation to get max heap
  heapq.heapify(pairs)

  return [heapq.heappop(res)[1] for _ in range(k)]


