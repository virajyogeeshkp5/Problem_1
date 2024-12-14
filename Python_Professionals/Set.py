# set
# Intersection
a={1,2,3,4,5}
b={3,4,5,6}
print(a&b)
print(a.intersection(b))

# union
print(a|b)

# difference
print(a-b)

# symetric difference
print(a^b)

print(a>=b)

print(a<=b)

print(a.isdisjoint(b))

print(2 in a)

print(2 not in a)

s={1,2,3}
s.add(4)
print(s)

s.discard(3)
print(s)

s.update({3,4})
print(s)

colour = ['red','green','yellow','oranbe','white']
one= set(colour)
print(one)
print(list(one))
print(list(set(colour)))

print(len(a))

print(len(b))

set1={'a','b','b','c'}
print(set1)

list1=['a','b','b','c']
print(list1)

from collections import Counter
countera = Counter(['a','b','b','c'])
print(countera)

