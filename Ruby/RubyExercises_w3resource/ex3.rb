# Write a Ruby program to create a new string which is n copies of a given string where n is a non-negative integer

def multiple_string(str, n)
  return str * n
end

puts multiple_string("a", 1)
puts multiple_string("a", 2)
puts multiple_string("a", 3)
puts multiple_string("a", 4)
puts multiple_string("a", 5)