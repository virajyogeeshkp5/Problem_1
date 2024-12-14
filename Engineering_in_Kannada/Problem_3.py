"""Character counter: write a python program that:
* Ask the user for a string
* prints how many character are in a string, excluding spaces."""

s = input("string:")
print(len(s.replace(" ","")))


