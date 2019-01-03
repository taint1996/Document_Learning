mark = 72

if mark > 50:
	if mark >= 80:
		print("You're A Grade")
	elif mark >= 60 and mark < 80:
		print("You got B Grade")
	else:
		print("You got C Grade")
else:
	print("Failed")


### not operator in if statement
mark = 100

if not(mark == 100):
  print("mark is not 100")
else:
  print("mark is 100")

### in operator
color = ["Red", "Blue", "Yellow"]
setColor = "Green"

if setColor in color:
  print("In here!")
else:
  print("Nothing to find")
