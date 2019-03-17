# While Loops
i = 0
numbers = []

# while i < 6
#   puts "At the top i is #{i}"
#   numbers << i

#   i += 1
#   puts "Number now: ", numbers
#   puts "At the bottom i is #{i}"
# end

# puts "The numbers: "

# numbers.each { |i| puts i}

for i in 0..6
  puts "Forloop At the top i is #{i}"
  numbers << i

  i += 1
  puts "Number now: ", numbers
  puts "At the bottom is #{i}, #{numbers}"
  i += 1
end
puts "The numbers: "

numbers.each { |i| puts i}
