"""Simple Greeting Program: Write a Python Program that asks the user for their name and age, that prints a persanalized greeting message
use both the + operator and f-strings for output."""

# Take a input value
name = input("Enter your name: ")
age = input("Enter your age: ")

# with out using f string
print("Hello "+name+ " your age is " +age+ " years old")

# using f string
print(f"Hello {name}  your age is {age}  years old")