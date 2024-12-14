# Create a python program to print 1 to 10
for i in range(1,11):
    print(i)

for i in range(1,11):
    print(i,end=" ")


# Create a python program to print multiples to given number up to n terms
M=int(input("Enter the number of multiple: "))
n=int(input("Enter the number of term: "))
for i in range(1,n+1):
    print(i*M,end=",")

# Create a python program to print sum of all even number from 11 to 50
sum=0
for i in range(11,51):
    if i%2==0:
        sum+=i
    print(sum)
