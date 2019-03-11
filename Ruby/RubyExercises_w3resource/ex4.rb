# Write a Ruby program which accept the radius of a circle from the user and compute the parameter and area
radius = 5.0
perimeter = 0.0
area = 0.0

print "Input the radius of the circle: "
radius = gets.to_f

perimeter = 2 * 3.14 * radius
area = 3.14 * (perimeter ** 2)

puts "The perimeter is #{perimeter} and the area is: #{area}"
