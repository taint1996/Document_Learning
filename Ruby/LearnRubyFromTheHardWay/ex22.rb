# Read some code in github
"Tai Beo".reverse # => oeB iaT
"40".reverse # only String can be reverse

# Hello abc
puts "abc".gsub("a", "xyz") # -> will return Hello xyz

poem = """
My toast has flown from my hand
And my toast has gone to the moon.
But when I saw it on television,
Planting our flag on Halley's comet,
More still did I want to eat it.
"""

poem.lines.reverse # return Array each line

puts "We can use .join("") to reverse Array to string"
puts poem.lines.reverse.join("\n")
