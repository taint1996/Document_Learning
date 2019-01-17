# Exercise 19: Functions and Variables
def cheese_and_crackers(cheese_count, box_of_crackers)
  puts "--------- Phomai & banh quy Programming ---------"
  puts "You have #{cheese_count} cheeses!"
  puts "You have #{box_of_crackers} boxes of crackers!"
  puts "That is enough for a party"
end

puts "We can just give the function numbers directly: "
cheese_and_crackers(20, 30)

puts "Or, we can use Variables from our scripts: "
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

puts "We can even do math inside too: "
cheese_and_crackers(10 + 20, 5 + 6)

puts "And we can combine the two, Variables and math: "
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
