"""Count Vowels in a String:

Write a program that counts how many vowels are in a given string using a for loop."""

vowels = "aeiou"
s="this is yogee"
count=0
for letters in s:
    if letters in vowels:
        count = count +1

print(count)
