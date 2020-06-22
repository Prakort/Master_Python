def solution(nums):
  hm = {}
  output = []
  for i in range(len(nums)):
    size = nums[i]
    if size not in hm:
      hm[size] = [i]
    else:
      hm[size].append(i)
    # we add into list to the result
    # when the size is reached max
    # reset the map
    if len(hm[size]) == size:
      output.append(hm[size])
      hm[size] = []
      
  return output
      
      
