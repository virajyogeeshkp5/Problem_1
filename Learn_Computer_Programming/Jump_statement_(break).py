for i in range(7,14):
    print("in the loop")
    print(i)
print("Loop successfully executed")

# Break Statement
for i in range(7,14):
    print("in the loop")
    if i%10==0:
        break
    print(i)
print("Terminated by break statement")

# while condition 
x=7
while x<14:
    print("in the loop")
    print(x)
    x+=1
print("Loop succesfully executed")

# while condition in break statement
x=7
while x<14:
    print("in the loop")
    if x%5==0:
        break
    print(x)
    x+=1
print("Terminated by break")
