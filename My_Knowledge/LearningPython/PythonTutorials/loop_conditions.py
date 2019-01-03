i = 1
while i < 6:
	print(i)
	i += 1

# Stop the loop if i is 3.

i1 = 1
while i1 < 6:
	if i1 == 3:
		break
	print("Stop loop in 3??", i1)
	i1 += 1


# Loop through the items in the fruits list.
fruits = ["Lemond", "Orange", "Banana"]

for x in fruits: 
	print(x)

# In the loop, when the item value is "banana", jump directly to the next item.

fruits1 = ["apple", "banana", "cherry"]

for x in fruits1:
	if x == "banana":
		continue
	print(x)

# Use the range function to loop through a code set 6 times.
for x in range(6):
	print("Loop range 6 times: ", x)
