# List

# Sum
l=[1,2,3,4,5,6,7,8,9]
print(sum(l))

# using for loop for sum
l=[1,2,3,4,5,6,7,8,9]
total=0
for num in l:
    total=total+num
    
print(total)

#1
l=[1,2,3,4,5,6,7,8,9]
total=0
for num in l:
    print(total)
    total=total+num
    
print(total)

# Doubling each number in a list
l=[1,2,3]
k=[]
for num in l:
    k.append(num*2)
print("double list:",k)

foods = ["dosa", "idly"]
for food in foods:
    print(f"I like food {food}")

student_marks = {"yogee":99, "viraj":85}
for student in student_marks:
    print(student)

student_marks = {"yogee":99, "viraj":85}
for student in student_marks.keys():
    print(student)

student_marks = {"yogee":99, "viraj":85}
for marks in student_marks.values():
    print(marks)

student_marks = {"yogee":99, "viraj":85}
for student, marks in student_marks.items():
    print(f"{student} - {marks}")

student = ["yogee", "veer", "hanuma"]
marks = [95, 89, 99]
student_marks = {}
for i in range(len(student)):
    student_marks[student[i]] = marks[i]
print(student_marks)

numbers = [1,2,3,4,5,6]
square = [num **2 for num in numbers]
print(square)

l=[x for x in range(1,11)]
dl=[x**2 for x in l]
print(dl)

# even number
l=[x for x in range(1,11)]
edl=[x**2 for x in l if x%2==0]
print(edl)


student = ["yogee", "veer", "hanuma"]
chr = [x[1] for x in student]
print(chr)

# upper
student = ["yogee", "veer", "hanuma"]
chr = [x.upper( ) for x in student]
print(chr)

numbers = [1,2,3,4,5]
square_dict = {num:num**2 for num in numbers}
print(square_dict)

student = ["yogee", "veer", "hanuma"]
chr = {x: len(student) for x in student}
print(chr)

city_population = {"Bengalore":95, "Tumkur":65, "bither":23}
high_population = {city:population for city, population in city_population.items( ) if population > 30}
print(high_population)

# string convert to list
s = "this is a book"
l = s.split()
print(l)

s = "this-is-a-book"
l = s.split("-")
print(l)

x = input("Enter the number: ")
print(x.split( ))


x = input("Enter the number: ").split( )
print(x)

x = input("Enter the number: ").split( )
l = [int(num) for num in x]
print(l)