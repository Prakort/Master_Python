def solution(nums, k):
  """
  rotate array with k steps
  it is the same, reverse the whole, reverse [0..k] and reverse [k..n]
  """
  n = len(nums)
  k %= n 

  # reverse the whole array
  reverse(nums,0,n-1,n)
  # reverse the first k
  reverse(nums,0,k-1)
  # reverse the the rest of array
  reverse(nums,k,n-1)

def reverse(nums, l , r, n):
  while l < r < n:
    nums[l], nums[r] = nums[r] , nums[l]
    l += 1
    r -=1

##### possible solution ######
# for i in range(k): nums.insert(0,nums.pop())
##### wow one line code

##### nums[:] = nums[n-k:] + nums[:n-k]
