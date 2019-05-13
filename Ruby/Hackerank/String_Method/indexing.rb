string = "Hello World!"
string[string.size - 1] # "!" 
string[-1] # "!"

str = "Hello"
str[str.size, 0] = " World!" # append by assigning at the end of the string -> "Hello World!"
str[5, 0] = "," # insert a comma after the 5th position
str[5, 6] = ""  # delete 6 characters starting from index 5. -> "Hello!"
str[5,1] = " World" # replace the string starting from index 5 and of length 1 with the given string. 

# In this challenge, your task is to code a serial_average method which is described below:

# It takes a fixed width string in format: SSS-XX.XX-YY.YY. SSS is a three digit serial number, XX.XX and YY.YY are two digit numbers including up to two decimal digits.
# It returns a string containing the answer in format SSS-ZZ.ZZ where SSS is the serial number of that input string, and ZZ.ZZ is the average of XX.XX and YY.YY.
# All numbers are rounded off to two decimal places.
def serial_average str
  digit1 = s[4..7]
  digit2 = s[9..-1]
  avg = (digit1 + digit2) / 2
end