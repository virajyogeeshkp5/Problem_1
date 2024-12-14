# Take the user input
# Take a string to user input
name=input("Enter your name:")
print("Your name is",name)

# Take a value to user input
a=int(input("Enter your age numeric: "))
print("Your age is",a)

# Add the the number of user in put
a=int(input("Enter your age: "))
print("your after birthday",a+1)

# Take percentage of user in put
a=float(input("Enter your percentage: "))
print("your percentage is:",a)

# Take 2 number and sum
A, B=input("Enter two value by separated: ").split()
print("sum is",int(A)+int(B))

# Take string and value
Name, Age=input("Enter your Name and Age by separated: ").split()
print("your name is:",Name ,"\n, your age after birthday:",int(Age)+1)

# Arithmetic Operator to take user input
a=float(input("Enter a value: "))
b=float(input("Enter b value"))
print("sum =",a+b)
print("difference =",a-b)
print("product =",a*b)
print("quotient =",a/b)
print("remainder =",a%b)
print("a raised to the poer b = ",a**b)
