# Create a program to accept the score betweeen 0 & 100 (both included) and print the following grade according to the range.
# average grade
# 90 above distingtion
# 60 to 89 first class
# 40 to 59 second class
# below 40 failed

score = int(input("Enter the score: "))
if score>=0 and score<=100:
    if score>=90:
        print("distingtion")
    elif score>=60 and score<=90:
        print("first class")
    elif score>=40 and score<=60:
        print("second class")
    else:
        print("filed")
else:
    print("invaled")

# 2.
score = int(input("Enter the score: "))    
if score>=0 and score<=100:
    if score>=40:
        if score>=60:
            if score>90:
                print("distingtion")
            else:
                print("first class")
        else:
            print("second class")
    else:
        print("failed")
else:
    print("invalid")