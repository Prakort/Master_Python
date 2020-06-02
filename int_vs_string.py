import functools
import string

def int_to_string(x):
  s = []
  isNegative = False
  if(x < 0):
    x, isNegative = -x , True

  while x != 0:
    s.append(chr(ord('0') + x % 10))
    x //=10

  return ('-' if isNegative else '') + ''.join(reversed(s))

a = int_to_string(9091111)
print(type(a))

def string_to_int(s):
  return functools.reduce(lambda running_sum, 
  c : running_sum * 10 + string.digits.index(c), s[s[0]== '-':],0) * ( -1 if s[0] == '-' else 1)

def string_to_int_two(s):
  n, isNegative = 0, s[0]== '-'
  copy = s[isNegative:]
  print(copy)
  for c in copy:
    # ord(char) return the unicode representing the 'char' - ord('0') will give the int of that numeric char
    n = n * 10 + ord(c) - ord('0')
    print(n)
  return n * (-1 if s[0] == '-' else 1)

print('string to int: ',string_to_int_two('220000'))

# s = '12345'
# print(s[True:])


# functools.reduce(function, iterable, initilizer=None):
# apply function with two arguments, reduce iterable to a sign value
# from left to right
