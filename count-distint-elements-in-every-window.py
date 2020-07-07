"""
Given an array of size n and an integer k, 
return the count of distinct numbers in all windows of size k.
"""
import collections
arr = [1, 2, 1, 3, 4, 2, 3]
k = 4
output = [3,4,4,3]


"""
Runtime: O(n)
Space: O(n)
"""
def solution(arr, k):
  hm = collections.defaultdict(int)
  res = []
  n = len(arr)

  for i in range(n):
    hm[arr[i]] += 1

    if i >= k:
      key = arr[i - k]
      hm[key] -= 1
      if hm[key] == 0:
        print(hm)
        del hm[key] # we have to del pair, zero value is still there

    # if the sum of the counts equals k
    # we have our window with k chars
    # we can check distint number of char is the key of map
    if sum(hm.values()) == k:
      res.append(len(hm))

  return res

print('res 1:', solution2(arr, k)) 
print('res 2:', solution2([1,2,4,4], 2)) 
print('res 3:', solution2([0,2,0,1,1,3], 3)) 




def test(nums, k):
  mapping = defaultdict(int)
  res = []
  for i in range(len(nums)):
      mapping[nums[i]] += 1

    if i >= k:
      if mapping[nums[i - k]] == 1:
        del mapping[nums[i - k]]
      else:
        mapping[nums[i - k]] -= 1

    if sum(mapping.values()) == k:
      res.append(len(mapping))

  return res
