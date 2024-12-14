for i in range(1,10):
    print(i)
else:
    (i,"is the last value of i")

# else using break statement
for i in range(1,10):
    print(i)
    if i%5==0:
        break
else:
    print(i,"is the last value i")

for i in range(1,10):
    print(i)
    if i%11==0:
        break
else:
    print(i,"is the last value of i")

# while condition
x=1
while x<6:
    print(x)
    x+=1
else:
    print(x,"is the last value of x")

x=1
while x<6:
    print(x)
    if x%3==0:
        break
    x+=1
else:
    print(x,"is the last value of x")

x=1
while x<6:
    print(x)
    if x%6==0:
        break
    x+=1
else:
    print(x,"is the last value of x")
    