# Dictionary in Python
birthday = {
    'chandan':"2022",
    'Darshan':"2023",
    'yogee':"2024"
}
print(birthday)
print(type(birthday))

print(birthday['yogee'])

# get
print(birthday.get("one","not found"))

birthday[1]="one"
print(birthday)

birthday.pop(1)
print(birthday)

del birthday["chandan"]
print(birthday)

print(birthday.keys())
print(birthday.values())
print(birthday.items())

num = {
    1:"one",
    2:"two",
    3:"three"
}
birthday.update(num)
print(birthday)

item1 = {
    "name":"yogee",
    "weight":1,
    "price":90.3
}

item2 = {
    "name":"gane",
    "weight":5,
    "price":91.3
}
items = [item1,item2]
print(f"total weight:{item1["weight"]+item2["weight"]}kg")