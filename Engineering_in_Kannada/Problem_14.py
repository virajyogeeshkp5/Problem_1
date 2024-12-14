"""Basic Dictionary Operations:

Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.
Add a new city and its dish to the dictionary.
Update the dish for Bengaluru.
Remove one city from the dictionary.
Use the keys() method to print all city names in the dictionary.
Use the values() method to print all dishes in the dictionary."""

dishes = { "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa",
    "Mandya":"Ragi mude",
    "Davanagere":"Bene Dosa"}

print(dishes)

dishes["Hassan"] = "idle" #add
print(dishes)

dishes["Bengaluru"] = "Bengaluru Bath" #Update
print(dishes)

del dishes["Mysuru"] #Remove
print(dishes)

print(dishes.keys())
print(dishes.values())




