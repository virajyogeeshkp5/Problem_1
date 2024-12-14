"""Logical Operater: Write a python program that takes two number that input from the user and checks if:
* Both numbers are greater than 10(using and)
* At least one of the number less than 5(using or)
* The first number is not greater than the second(using not)"""

a=int(input("Enter the number: "))
b=int(input("Enter the number: "))

print(a>10 and b>10)
print(a<5 or b<5)
print(not(a>5))
