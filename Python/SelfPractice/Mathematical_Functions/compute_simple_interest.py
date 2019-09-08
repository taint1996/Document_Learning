# 1.	Take in the values for principle amount, rate and time.
# 2.	Using the formula, compute the simple interest.
# 3.	Print the value for the computed interest.
# 4.	Exit.

principle = float(input("Enter the principle amount: "))
time = int(input("Enter the time(years): "))
rate = float(input("Enter the rate: "))
simple_interest = (principle * time * rate) / 100
print("The simple interest is: ", simple_interest)
