# Exercise 21: Functions Can Return Something
def add(a, b)
  puts "Adding #{a} + #{b}"
  return a + b
end

def substract(a, b)
  puts "Subtracting #{a} - #{b}"
  return a - b
end

def multiply(a, b)
  puts "Multiplying #{a} * #{b}"
  return a * b
end

def divide(a, b)
  puts "Deviding #{a} / #{b}"
  return a / b
end

puts "Let's do some math with just functions!"

age = add(30, 5)
height = substract(86,4)
weight = multiply(54, 2)
iq = divide(100, 2)

puts "Age: #{age}, Height: #{height}, Weight: #{weight}, IQ: #{iq}"

puts "Here's a puzzle." # puzzle = cau do

what = add(age, substract(height, multiply(weight, divide(iq,2))))
puts "That become: #{what}. Can you do it by hand?"

puts "Here's another puzzle." # puzzle = cau do
another_what = add(24, 34/100 - 1023)
puts "That become: #{another_what} ^^"
