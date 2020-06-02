# Map
# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)

a = dict(one = 1, two = 2, three = 3)
b = {'one' : 1, 'two' : 2, 'three' : 3}
c = dict(zip(['one', 'two', 'three'], [1,2,3]))
d = dict([('one',1),('two',2),('three',3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

print( a == b == c == d == e)

# list(d) return a list of all keys
li = list(a)
print('list(d)',list(li),'len(d)', len(li))

el = d['one']
print(el)
b = a
del a['one']
print('shallow copy')
print('del a["one"]',a , 'b := a ',b)

# key not in dict 
# key is not in dict is wrong
print( 'two' not in a)

print('iter(d)', iter(a.keys()))


print(type(None))
