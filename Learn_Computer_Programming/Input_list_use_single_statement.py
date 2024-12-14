# Inputting a list using single statement and using loop
L1=[]
for i in range(4):
    x=input('Enter the element: ')
    L1.append(x)
print(L1)

# while
L1=[]
c='Y'
while c=='Y':
    x=input('Enter the element: ')
    L1.append(x)
    c=input('To continue to print Y: ').upper()
print(L1)

# eval
L1=eval(input('Enter a list: '))
print(L1)
