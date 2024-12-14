# Functions
a,b=1,2
print(a+b)

c,d=3,4
print(c+d)

def greet():
    print("Hi hello world!")
greet()

def greet(boy, girl):
    print(f"Boy is {boy}")
    print(f"Girl is {girl}")
    print(f"{boy} friend {girl}")
greet("yogee", "yogi")

def table(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")
table(5)
table(6)
table(7)

# default parameter
def greet(boy, girl='girl'):
    print(f"Boy is {boy}")
    print(f"Girl is {girl}")
    print(f"{boy} friend {girl}")
greet("yogee")

def func(num):
    print(str(num)*3)
func(2)

def func(num):
    print(int(str(num)*3))
func(2)

def func(num):
    return int(str(num)*5)
a=100
b=func(20)
c=a+b
print(c)

def def_info(name, age):
    print(f"Name:{name} age:{age}")
def_info("yogee",30)

def add(a, b):
    return(a+b)
c=add(3, 2)
print(c)

