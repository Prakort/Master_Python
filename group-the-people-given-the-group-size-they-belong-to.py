def solution(nums):
  hm = {}
  output = []
  for i in range(len(nums)):
    size = nums[i]
    if size not in hm:
      hm[size] = [i]
    else:
      hm[size].append(i)
  
    if len(hm[size]) == size:
      output.append(hm[size])
      hm[size] = []
      
  return output
      
      
