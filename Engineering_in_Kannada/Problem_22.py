"""Countdown Timer:

Write a program that counts down from 10 to 1 using a while loop and prints "Happy New Year!" after the countdown is over."""

import time
i=10
while i>0:
    time.sleep(1)
    print(i)
    i=i-1
print("Happy New Year!")
