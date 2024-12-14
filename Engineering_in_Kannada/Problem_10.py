"""Revers and Sort a list: Create a list of numbers 
* sort it in decending order.
* Reverse the sorted list and print it."""

l=[22, 25, 35, 20, 100]
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)

# 2nd option
l.sort()
l.reverse()
print(l)
