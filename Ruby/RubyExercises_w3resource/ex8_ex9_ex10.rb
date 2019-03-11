#  Write a Ruby program to check two integer values whether either of them is in the range 20..30 inclusive.
def in2030(a, b)
  return (a >= 20 && a <= 30) || (b >= 20 && b <= 30)
end

puts "Is in the range 20 to 30: " + in2030(15, 50).to_s
puts "Is in the range 20 to 30: " + in2030(15, 25).to_s

# Write a Ruby program to check three numbers and return true if one or more of them are small. A number is called "small" if it is in the range 1..10 inclusive.
def in1to10(a, b, c)
  return (a >= 1 && a <= 10) || (b >= 1 && b <= 10) || (c >= 1 && c <= 10)
end

puts "Is in the range 1 to 10: " + in1to10(15, 50, 20).to_s
puts "Is in the range 1 to 10: " + in1to10(1, 50, 20).to_s
puts "Is in the range 1 to 10: " + in1to10(10, 50, 20).to_s

def checkOneOrOtherIsSmall(a, b)
  return (((a >= 1 && a <= 10) && !(b >= 1 && b <= 10)) || (!(a >= 1 && a <= 10) && (b >= 1 && b <= 10)));
end

puts checkOneOrOtherIsSmall(12, 15)
puts checkOneOrOtherIsSmall(10, 20)
