"""List Manipulation:
* create a list of 5 items(strings or numbers).
* Add a new item to the end of the list and another at the second position.
* Remove the third item from the list.
* print the list after each operation."""

l = [1, "a",100,True,5]
l.append("end")
l.insert(1,"insert_here")
l.remove(l[2])
print(l)
