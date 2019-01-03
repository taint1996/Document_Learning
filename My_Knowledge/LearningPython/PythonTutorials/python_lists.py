########### Create a List
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Print the second item of the list
print("The second item of the list is ", thislist[1])

# Change the second item:
thislist[1] = "blackcurrant"
print(thislist)

########### Loop through in List
for x in thislist: 
	print(x)

car = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964
}
# --> Use the get method to print the value of the "model" key of the car dictionary.
print(car.get("model"))

# Change the "year" value from 1964 to 2018.
car["year"] = 2018
print(car)

# Add the key/value pair "color" : "red" to the car dictionary.
car["color"] = "red"
print(car)

# Use the pop method to remove "model" from the car dictionary.
car.pop("model")
print(car)

# Use the clear method to empty the car dictionary.
car.clear()
print(car)


############# ADD ITEMS
thislist1 = ["apple", "banana", "cherry"]

# Using the append() method to append an item:

thislist1.append("orange")
print(thislist1)

# Insert an item as the second position:

thislist1.insert(2, "orange") # --> 2 is n position
print(thislist1)

########## Remove Items
#(1) The remove() method removes the specified item:
thislist1.remove("banana")
print(thislist1)

#(2) The pop() method removes the specified item:
thislist1.pop()
print(thislist1)

#(3) The del method removes the specified item:
del thislist1
print(thislist1)
