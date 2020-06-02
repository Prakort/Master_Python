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
  
# start_time =  time.time()
# int_to_string_func(number)
# end_time =  time.time()
# print('fast',end_time - start_time)

# != not equal
# is object identity 
# is not negated object identity
a = [1,2,3,4,5,6,7]
b = a 
# b is a reference of a and have the same value and they are the same object
print('==', a == b , 'vs is', a is b)
c = [1,2,3,4,5,6,7]
# c has the same value as a but c is not the same object as a
print('==', a == c , 'vs is', a is c)
# del i to j and k skip
del a[1:6:2]
# list.append(x) := a[len(a):len(a)] = [x] <= must be iteratable
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
# list.sort(key=function) key is a function return which element that the list will sort by
students.sort(key= lambda student: student[2])
print(students)
# using operator.itemgetter or attrigetter to sort by more than 1 element
students.sort(key=operator.itemgetter(0,1))
print(students)

a = 'signle quotes string'
b = "double quotes string"
c = """ tripple quotes string"""
d = ''' tripple quotes string '''
print('str.count(sub[start:end])',a.count('si'))
print('str.endswith(suffix)', a.endswith('string'))

# str.format 
print('{} is the signle quotes string {}'.format(a,2))

# str.format
print('{e} if e is not defined not missing value we could use format to give default value'.format(e='John as default value'))

# str.isascii()
print('str.isascii()',"007F".isascii()) 
# str.isdecimal()
print('str.isdecimal()','090'.isdecimal()) 
# str.isdigit()
print('str.isdigit','090'.isdigit())
# str.isnumeric()
print('str.isnumberic()', '033333'.isnumeric())
# This link below has awesome examples of the differences between these 3
# https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-python

# str.title() => first char of each word to upper case
print('Make a title with str.title()','this is awesome'.title())
