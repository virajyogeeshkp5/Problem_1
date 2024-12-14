st=input("Enter the string: ")
for i in st:
    print(i)

st=input("Enter the string: ")
for i in st:
    print(i+'s',end=" ") 

# while

st=input("Enter the string: ")
y=len(st)
print(y)
ind=0
while ind<y:
    print(st[ind])
    ind+=1   

# for range
st=input("Enter the string: ")
ind=0
for i in range(len(st)):
    print(st[i])
    