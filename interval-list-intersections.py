def solution(A, B):
  """
  (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
  A: [0,5]
  B: [3,6]
  intersection is [3,5]
  [max(start),min(end)]
  """

  i = j = 0
  result = 0

  while i < len(A) and j < len(B):
    lo = max(A[i][0], B[j][0])
    hi = max(B[j][1], A[i][1])

    if lo < hi:
      result.append([lo, hi])
    # skip the smallest end
    if hi != A[i][1]:
      j +=1
    else:
      i +=1
