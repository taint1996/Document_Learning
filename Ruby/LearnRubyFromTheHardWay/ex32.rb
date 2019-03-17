# Loops and Array
the_count = [1, 2, 3, 4, 5]
fruits = ["apple", "orange", "pears", "apricots"]
change = [1, "penies", 2, "quarters"]

for number in the_count
  puts "There is count #{number}"
end

fruits.each do |fruit|
  puts "A fruits of type #{fruit}"
end

change.each { |i| puts "I got #{i}"}

elements = []

(0..5).each do |i|
  puts "adding #{i} to the list"
  elements << i # elements.push(i)
end

elements.each { |i| puts "Element was #{i}"}
