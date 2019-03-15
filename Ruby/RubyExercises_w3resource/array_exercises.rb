fruit_string = "boulder, apple, banana, peach, cow"
# output: "apple, banana, peach"
fruits = fruit_string.split(',')
getHead = fruits.shift
getLast = fruits.pop
puts fruits_string = fruits.join(',')

# Write a method named with_these_numbers so that the following code will work:
# with_these_numbers(1, 4) do |first, second|
#     puts first + second # Output: 5
# end
def with_these_numbers(first_number, second_number)
    yield first_number, second_number
end

# IRB session
numbers = [3, 29, 5, 12, 18]
multiple = numbers.each { |number| puts number**2 }
isOdd = numbers.each { |number| puts number.odd? }
isEven = numbers.each { |number| puts number.odd? }

strings = ["I", "ma", "a", "ybuR", "retsam"]
reverse_strings = strings.each { |i| puts i.reverse }