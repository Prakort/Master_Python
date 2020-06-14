def solution(digits):
  phone = {
    '2': ['a','b','c'],
    '3': ['d','e','f'],
    '4': ['g','h','i'],
    '5': ['j','k','l'],
    '6': ['m','n','o'],
    '7': ['p','q','r','s'],
    '8': ['t', 'u', 'v'],
    '9': ['w','x','y','z']
  }

  result = []
  backtrack(digits, '', result, phone)
  return result

def backtrack(digits, combination, result, phone):
  # base case 
  # when no more digit to look up
  # add the combination into the list
  if not digits:
    result.append(combination)

  # iterate over the map of the digits
  for letter in phone[digits[0]]:
    # for each letter, start with the next digit 
    # concatenate the letter to the previous combination
    backtrack(digits[1:], combination + letter, result, phone)
  
