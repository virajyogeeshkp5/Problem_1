for i in range(12,20):
    print("in the loop")
    if i%2==0:
        continue
    print(i)
print("Loop Complited")

# while condition
x=12
while x<20:
    print(x)
    x+=1
print("Loop complited")

# while condition in continue statement
x=11
while x<20:
    x+=1
    if x%2==0:
        continue
    print(x)
print("Loop Complited")
