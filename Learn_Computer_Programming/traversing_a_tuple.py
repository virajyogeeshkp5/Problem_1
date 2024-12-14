vow=('a','e','i','o','u')
for i in vow:
    print(i)

for i in range(len(vow)):
    print(vow[i])

for i in range(-1,-len(vow)-1,-1):
    print(vow[i])

# while
vow=('a','e','i','o','u')
ind=0
while ind<len(vow):
    print(vow[ind])
    ind+=1

vow=('a','e','i','o','u')
ind=-1
while ind<-len(vow):
    print(vow[ind])
    ind-=1

vow=('a','e','i','o','u')
ind=-1
while ind<-len(vow):
    print(vow[ind],end=',')
    ind-=1