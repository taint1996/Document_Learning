#----------------------------------------#
# Question 1:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
l = []

for i in range(2000, 3200):
  if(i % 7 == 0) and not (i % 5 == 0):
    l.append(str(i))
print(','.join(l))

#----------------------------------------#
# Question 2:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
def factorial(x): # Tinh giai thua
  if x == 0:
    return 1
  return x * factorial(x - 1)
print("Question 2: ", factorial(5))

#----------------------------------------#
# Question 3:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
d = dict()

for i in range(1, 10):
  d[i] = i * i
print(d)

#----------------------------------------#
# Question 4:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
values= ['34', '67', '55', '33', '12', '98']
t=tuple(values) # tuple return [] -> ()
print(t)

#----------------------------------------#
# Question 5
# Level 1

# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters

class InputOfString:
  def __init__(self):
    self.s = ""

  def getString(self):
    self.s = "Abcd"
    print(self.s)

  def printStringUpper(self):
    print(self.s.upper())

strObj = InputOfString()
strObj.getString()
strObj.printStringUpper()

#----------------------------------------#
# Question 6
# Level 2

# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

# Hints:
# If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
# In case of input data being supplied to the question, it should be assumed to be a console input.
import math
c = 50
h = 30
value = []
items = [x for x in range(1, 100)]

for d in items:
  value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))

#----------------------------------------#
# Question 7

# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

dimension = [int(x) for x in range(1,10)]
print("Dimensional: ", dimension)

colNum = dimension[0]
rowNum = dimension[1]

multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
  for col in range(colNum):
    multilist[row][col] = row * col
print(multilist)
