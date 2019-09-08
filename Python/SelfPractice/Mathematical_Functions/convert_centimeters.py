# This is a Python Program to read height in centimeters and then convert the height to feet and inches
# 1.	Take the height in centimeters and store it in a variable.
# 2.	Convert the height in centimeters into inches and feet.
# 3.	Print the length in inches and feet.
# 4.	Exit.

cm = int(input("Enter height in centemeters: "))
inches = 0.394 * cm
feet = 0.0328 * cm

print("The length in inches: ", round(inches,2))
print("The length in feet: ", round(feet, 2))

