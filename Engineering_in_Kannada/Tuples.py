# Tuples in Python

genders = ("male","female","others")
print(genders)
print(type(genders))
print(len(genders))

print(genders[0])
print(genders[1])
print(genders[2])

print(genders[-1])
print(genders[-2])
print(genders[-3])

print(genders[1:3])

# combined tuple
tuple1=(1,2,3)
tuple2=(4,5,6)
combined_tuple=tuple1+tuple2
print(combined_tuple)

# repetated tuple
repetated = (4,5,6) * 3
print(repetated)

# checking
fruits = ("apple","mango","graps")
print("apple" in fruits)

# count tuple
my_tuple = (1,2,4,2,1,1,1)
print(my_tuple.count(1))
print(genders.count("male"))

# index
print(fruits.index("mango"))
print(genders.index("male"))

