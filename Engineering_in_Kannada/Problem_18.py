"""Simple Eligibility Check:

Write a program that checks whether a person is eligible for a library membership. 
If they are under 18, they get a student membership. 
If they are 60 or older, they get a senior citizen membership. Otherwise, they get a regular membership."""



age = int(input("Enter your age: "))
if age <18:
    print("Get a Student Membership")
elif age >=60:
    print("Get a senior citizen Membership")
else:
    print("Get a Regular Membership")
