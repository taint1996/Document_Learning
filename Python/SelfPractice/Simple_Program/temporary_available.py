# This is a Python Program to exchange the values of two numbers without using a temporary variable.

# Problem Description
# The program takes both the values from the user and swaps them without using temporary variable.

# Problem Solution
# 1.	Take the values of both the elements from the user.
# 2.	Store the values in separate variables.
# 3.	Add both the variables and store it in the first variable.
# 4.	Subtract the second variable from the first and store it in the second variable.
# 5.	Then, subtract the first variable from the second variable and store it in the first variable.
# 6.	Print the swapped values.
# 7.	Exit.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num1 = num1 + num2
print(num1)
num2 = num1 - num2
print(num2)
num1 = num1 - num2
print(num1)

print("a is: ", num1, "b is: ", num2)