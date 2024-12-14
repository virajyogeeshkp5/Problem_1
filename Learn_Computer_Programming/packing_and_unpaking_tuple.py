# packing and unpacking tuples
# packing
p=20
q=40
r=60
tup1=(p,q,r)
print(tup1)

# unpacking
tup2=('hendry','abdul','surya',500,600,400)
a1,a2,a3,a4,a5,a6=tup2
print(a6)
print(a3)
print(tup2)

*names,a1,a2,a3=tup2
print(names)

print(a2)

n1,n2,n3,*v=tup2
print(n1)

print(v)

a1,*a2,a3=tup2
print(a1)
print(a2)
print(a3)
