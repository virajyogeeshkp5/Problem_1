# if elif and else condetion statements
x=10
if x==10:
    print("yes x is 10")

x=24
if x%2==0:
    print("x is even")

x=23
if x%2==0:
    print("x is even")
else:
    print("x is odd")

signal = "red"
if signal=="red":
    print("stop")
else:
    print("go")

signal = "yellow"
if signal=="red":
    print("stop")
elif signal=="yellow":
    print("start")
else:
    print("go")

signal = input("what is the color of signal:" )

if signal=="red":
    print("stop")
elif signal=="yellow":
    print("start")
else:
    print("go")

att=75
if att>=75:
    print("exam")
else:
    print("no exam")
