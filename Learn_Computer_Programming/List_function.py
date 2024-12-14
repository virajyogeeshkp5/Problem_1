Li=[1,2,3,4,5,6]
print(Li)

Li.clear()

print(Li)

Li_1=[1,2,3,5,6,3,2,1,5,9,8,7,3,2,1]
print(Li_1)

print(Li_1.count(3))

print(Li_1.count(1))

Li_1.reverse()
print(Li_1)

Li_1.sort()
print(Li_1)

Li_1.sort(reverse=True)
print(Li_1)

sorted(Li_1)
print(Li_1)

sorted(Li_1,reverse=True)
print(Li_1)

Lis=['ab','aa','xyz','hello']
Lis.sort()
print(Lis)

Li_1.extend(Lis)
print(Li_1)
