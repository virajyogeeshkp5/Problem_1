# Python Sets
fruits_sets = {"apple","bannana","mango","cherry"}
print(fruits_sets)
print(type(fruits_sets))

numbers_sets = {1,2,3,4,5,6,7,8,9,10}
print(numbers_sets)
print(type(numbers_sets))

empty_set = set( )
print(empty_set)
print(type(empty_set))

s={1,2,3}
print(s)

s={20,2,123} # unorder
print(s)

s1 = {1,2,3}
s2 = {3,4,5}
print(s1|s2) # union
print(s1 & s2) # intersection
print(s1 - s2) # difference

s={1,2,3}

s.add(4)
print(s)




