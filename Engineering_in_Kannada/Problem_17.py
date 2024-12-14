"""Meal Time Checker:

Create a program that checks the time of day (24-hour format) and prints whether it's time for breakfast, lunch, or dinner.
Breakfast: 8 AM
Lunch: 1 PM
Dinner: 8 PM
If none of these times, print "It's not meal time."""

time = int(input("Enter the time: "))
if time==8:
    print("It's Breakfast time")
elif time==1:
    print("It's Lunch time")
elif time==8:
    print("It's Dinner time")
else:
    print("It's not meal time")
    