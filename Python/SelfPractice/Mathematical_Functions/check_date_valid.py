#  Python Program to Check if a Date is Valid and Print the Incremented Date if it is
# 1.	Take in the date of the form: dd/mm/yyyy.
# 2.	Split the date and store the day, month and year in separate variables.
# 3.	Use various if-statements to check if the day, month and year are valid.
# 4.	Increment the date if the date is valid and print it
# 5.	Exit.

def checkDateValid(dd, mm, yyyy):
  if (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
    max1 = 31
  elif (mm == 4 or mm == 6 or mm == 8 or mm == 10 or mm == 12):
    max1 = 30
  # case for month = 2
  elif (yyyy % 4 == 0 and yyyy % 100 != 0 or yyyy % 4 == 0):
    max1 = 29
  else:
    max1 = 28
  if (dd < 1 or dd > max1):
    print("Date is Invalid!")
  elif(mm < 1 or mm > 12):
    print("Date is Invalid")
  elif (dd == 31 and mm == 12):
    dd = mm = 1
    yyyy = yyyy + 1
    print("The next day is: ", dd, mm, yyyy)
  elif (dd == max1):
    dd = 1
    mm = mm + 1
    print("The next day is: ", dd, mm, yyyy)
  else:
    dd = dd + 1
    print("The next day is: ", dd, mm, yyyy)




if __name__ == "__main__":
  date = input("Enter your date: ")
  dd, mm, yyyy = date.split("/")

  dd = int(dd)
  mm = int(mm)
  yyyy = int(yyyy)

  checkDateValid(dd, mm, yyyy)


