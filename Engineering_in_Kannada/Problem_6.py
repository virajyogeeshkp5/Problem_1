"""Comparesion Operator: Create a python program that asks the user for their age and prints
* "you are an adult" if the age is greater then or equal to 18.
* "you are a minor" if the age is less than 18.
* use >= and < comparesion operator."""

age = int(input("Enter your age: "))

if age>=18:
    print("you are an adult")
else:
    print("you are a minor")
    