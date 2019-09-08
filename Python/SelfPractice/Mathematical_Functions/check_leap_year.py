# This is a Python Program to check whether a given year is a leap year or not.

# Problem Description
# The program takes in a year and checks whether it is a leap year or not.

# Problem Solution
# 1. Take the value of the year as input
# 2. Using an if-statement, check whether the year is a leap year or not
# 3. Print the final result
# 4. Exit

year = int(input("Enter the year you want: "))

if (year % 4 and year % 100 != 0 or year % 4 == 0):
  print("Leap year!")
else:
  print("The year isn't a leap year!")