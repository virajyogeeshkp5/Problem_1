"""Ticket Booking Simulation:

Write a program that simulates a bus ticket booking system. 
The bus has 8 seats. Each time a seat is booked, the available seats decrease. 
When there are no seats left, the loop stops and displays a message saying "All seats are booked."""

seats = 8
while seats>0:
    print("Book one seat")
    seats = seats -1
    print("Remaining seats:",seats)
print("All seats are booked")

