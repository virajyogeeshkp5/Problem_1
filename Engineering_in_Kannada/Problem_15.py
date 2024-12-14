"""Nested Dictionary Practice (Simple for now):

Create a dictionary to store details of two of your friends, including their names, favorite subject, and favorite food.
Access and print the favorite food of one friend."""

d= {
    "friend_1":{
        "names":"Yogee",
        "favorite_sub":"Python",
        "favorite_food":"Apple"
    },
      "friend_2":{
        "names":"Hanuma",
        "favorite_sub":"SQL",
        "favorite_food":"Mango"
        }
}

print(d)

f=d["friend_1"]
print(f["favorite_food"])

#step2
print(d["friend_1"]["favorite_food"])


