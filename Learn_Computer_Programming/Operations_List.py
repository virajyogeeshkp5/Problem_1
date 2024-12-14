# Operations on List
x=[1,2,3,4,5]
print(5 in x)

L1=[1,2,3,4,5,6]
L2=[10,20,30,40]
print(L1+L2)

L3=L1+L2
print(L3)

print(L2*3)

print(L1>L2)

L1[0]=60
print(L1)

print(L1>L2)

s=['abcd','mno','pqr']
s1=['ab','bc']
print(s>s1)

s1.insert(0,'abcd')

print(s1)

print(s1<s)

s1.insert(1,'xyz')
print(s1)

print(s>s1)

s2=['abcd','mno','pqr']
print(s)
print(s2>s)
print(s2==s)
print(s1!=s)
print(s2!=s)
print('xyz'in s1)
print('op' in s1)
print('pq' not in s1)
print(s1)

# Slicing a List
Lang=['py','java','c','c++','basic','vb','pearl']
print(Lang[2:5])
print(Lang[-2:-6:-1])
print(Lang[ :3])
print(Lang[ 3:])
print(Lang[ 6:2])
print(Lang[ -4:-1:-1])
print(Lang[ 0:5:2])
print(Lang[ -2:-6:-2])
print(Lang[ : :-1 ])

# Copy
Num = [1,2,3,4,5]
N=Num
print(id(Num))
print(id(N))
N.append(70)
print(N)
print(Num)
N1=Num.copy()
print(id(N1))
N1.append([20,30])
print(N1)
print(Num)

# del
ch=['a','b','c','d','e','f','g','h','i','j']
del ch[6]
print(ch)

del ch[3:7]
print(ch)

num=[1,2,3,4,5,6,7,8,9,10]
del num[0:10:3]
print(num)


