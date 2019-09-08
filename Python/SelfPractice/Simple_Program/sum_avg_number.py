# This is a Python Program to Calculate the Average of Numbers in a Given List.

# Problem Description
# The program takes the elements of the list one by one and displays the average of the elements of the list.

# Problem Solution
# 1.	Take the number of elements to be stored in the list as input.
# 2.	Use a for loop to input elements into the list.
# 3.	Calculate the total sum of elements in the list.
# 4.	Divide the sum by total number of elements in the list.
# 5.	Exit.

n = int(input("Enter your number: "))

for i in range(0, n):
  arr = []
  elem = int(input("Enter element: "))
  arr.append(elem)

avg = sum(arr) / n
print("Average number of list: ", round(avg, 2))