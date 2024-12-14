"""Tuple and Set Comparison:

Create a list of elements and convert it into both a tuple and a set.
Print both the tuple and the set.
Try to add new elements to the tuple and set. What differences do you observe?"""

l=[1,2,3,4,5,6]
t=tuple(l)
s=set(l)
print(t, s)
s.add(56)
print(s)
