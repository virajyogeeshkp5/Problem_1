# Create a python program to print 1 to 10
x=1
while x<=10:
    print(x)
    x+=1

# Create a python program to print multiples to given number up to n terms
M=int(input("Enter the multiple: "))
n=int(input("Enter the number of multiple: "))
x=1
while x<=n:
    print(x*M,end=",")
    x+=1

# Create a python program to print sum of all even number from 11 to 50
x=11
Sum=0
while x<=50:
    if x%2==0:
        Sum+=x
    x+=1
print("sum of all even number 11 to 50:",Sum)


