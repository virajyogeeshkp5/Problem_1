def great(a,b):
    if (a>b):
        print(a,"is greater")
        d=a-b
    else:
        print(b,"is greater")
        d=b-a
    print(d,"is defference between",a,"and",b)
n1=int(input("Enter the First number: "))
n2=int(input("Enter the second number: "))
great(n1,n2)