def solution(str):
  '''
  method: sliding window with left and right pointer
  we check the substring [left : right + 1] while increment the right by 1
  [left : right + 1] is substring from left index up to right index by checkig
  str[right + 1] which is the next char in the string.

  if the next char on the right is not in the prev substring 
  we have a new subtring without repeating char then
  - increment the right pointer
  - increment the counter of char
  - update the max between max and count 

  otherwise, the next right char is found in the substring
  - increment the left pointer to move the sliding window
  - decrement the counter of the char since we are not moving to the right but 
  moving only the left pointer only


  runtime: O(N^2) why ? : the whole string with len(n) is being iterated over 
  and we look up a char in the substring which is O(n) ===> max len of substring is n 
  then the runtime is O(N^2)

  space: O(1), we are not using any extra space
  '''
  lens = len(str)
  if lens == 1:
    return 1

  right = left = result = count = 0

  while left < lens and right < lens -1 :
    if str[right + 1] not in str[left : right + 1]:
      count +=1
      right +=1
      result = max(result, count)
    else:
      left +=1
      count -=1

  return result

def solution2(str):
  """
  using sliding window to check the repeating char

  first we have left and right pointer that start from index 0 
  every iteration we check if the char of the right index is already in the set

  if the right char is not in the set:
  - add the char into the set 
  - increment the right index
  - update the count of the char in the set use Right - Left O(1), lens(set) O(n)

  otherwise, the right char already exists in the set:
  - remove the right char but which index ? we keep moving to the right and if 
  we found a repeating char that mean it is same to the left most index then 
  we remove str[left] char
  - increment the left pointer, we want to check the next substring

  runtime: O(N), the whole string is iterated and looking up an char in the set is O(1)
  space: O(N), worst case, the whole string is stored in the set
  """
  lens = lens(str)

  sets = set()
  left = right = res = 0 

  while right < lens:
    if s[right] not in sets: 
      sets.add(s[right])
      res = max(res, right - left + 1)
      right +=1
      
    else:
      sets.remove(s[left])
      left +=1
  return res
