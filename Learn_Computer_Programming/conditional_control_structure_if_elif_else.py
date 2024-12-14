# 1.Create a python program to desplay whether the number given by the user is positive or negative
num=float(input("Enter the number: "))
if num>0:
    print(num,"is positive")
elif num<0:
    print(num,"is negative")
else:
    print(num,"is either positive or negative")

# 2.create a python program to accept a character and display whether the input character uppercase/lowercase/digit or any symbol
chr=input("Enter the character: ") 
if ord(chr)>=60 and ord(chr)<=90:
    print(chr,"is upper case")
elif ord(chr)>=97 and ord(chr)<=122:
    print(chr,"is lower case") 
elif ord(chr)>=48 and ord(chr)<=57:
    print(chr,"is a digit") 
else:
    print(chr,"is a symbol")
    