"""String Manipulation: Write a Python Program that:
* Take a sentence as input from the user.
* Print the sentence all uppercase and lowercase.
* Replace all spaces with underscore.
* Removes leading and trailing whitespaces."""

s=input("Enter sentence:" )
print(s.upper( ))
print(s.lower())
print(s.replace(" ","_"))
print(s.strip())
