# Write a Ruby program to create a new string where "if" is added to the front of a given string. If the string already begins with "if", return the string unchanged.
def if_string(str)
    str[0, 3] == "if " ? str : "if " << str 
end

puts("If string show: ", if_string("if else"))
puts("If string show: ", if_string("else"))