from copy import deepcopy
import copy
import bisect
from datetime import datetime
import time

a = [1,2,3,4,5,6,7]
i = 0, 
print(a[::-1])
print(a[::-1])
b = a[:3]+  a[3:] 
print(b)

c = list(map(lambda x: x**2, a))
print("c",c)

a = "owowowo"

def is_palindrom(s):
  return all(s[i] == s[~i] for i in range(len(s)//2))

print(is_palindrom(a))

# print(9/2, "vs" 9.0//2)

# it takes O(n2) since a new array of characters is creating when 
# appending the char
a = a[:]
print("a",a)
# to fix this problem, use list instead 

#Chapter 3 String

# chr(i) return a character (a string) from an interger that is unicode represent the character
# chr(65) = A
#
# ord(i) return an integer representing the Unicode character
# ord('A' = 65
def int_to_string(x):
  is_negative = False
  if( x < 0):
    x, is_negative = -x, True
  s = []
  while x is not 0:
    s.append(chr(ord('0') + x % 10))
    # print(x%10)
    x /= 10

  return ('-' if is_negative else '') + ''.join(reversed(s))

def int_to_string_slow(x):
  s = ''
  if( x < 0):
    s = s+ '-'
    x = -x
  while x != 0:
    remainder = x % 10
    x /= 10
    s += str(remainder)
  return s[::-1]

number = -90909299293
start_time = time.time()
str(number)
end_time = time.time()
print('slow',end_time - start_time)


def int_to_string_func(x):
  s = []
  is_negative = False
  if( x < 0):
    x, is_negative = -x, True
  while x != 0:
    s.append(chr(ord('0') + x%10))
    x /= 10

  return ('-' if is_negative else '') + ''.join(reversed(s))
  
start_time =  time.time()
int_to_string_func(number)
end_time =  time.time()
print('fast',end_time - start_time)

# != not equal
# is object identity 
# is not negated object identity
a = [1,2,3,4,5,6,7]
del a[1:6:2]
a.append(100)
a[len(a):len(a)] = [1000]
# list.clear() := del list[:]
del a[:]
t = [100,222,333,444]
a.extend(t)
a.remove(100)
# list.pop(index) retrieves the item at index and removes it
# list.remove(element) remove the first item == element in the list
a.reverse()

# list.reverse() vs reversed(string) they are different
print(a)

students = [
  ('a', 1, 'ZZZ'),
  ('a', 99, 'AAA'),
  ('z', 1, 'bbb')
]
import operator
students.sort(key= lambda student: student[2])
print(students)
students.sort(key=operator.itemgetter(0,1))
print(students)
