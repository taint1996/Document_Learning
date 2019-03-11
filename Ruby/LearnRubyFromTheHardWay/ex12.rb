# Exercise 12: Prompting People for Numbers
print "Give me your phone number: "
number = gets.chomp.to_i

bigger = number * 100
puts "A bigger number is #{number}"

print "Give me another number: "
another = gets.chomp
number = another.to_i

smaller = number / 100
puts "A smaller number is #{smaller}."

print "How much money you want? "
money = gets.chomp
number = money.to_f
cash = number / 10
puts "Cash is #{cash}."
