# class set([iterable])
# class frozenset([iterable])
# x in s
# x not in s
# isdisjoint

A = set([1,3,4,5])
B = set([2])
print('A.isdisjoint(B)',A.isdisjoint(B))

A.add(2)
A.remove(3)
A.discard(10)
A.pop()
A.clear()
print(A)
