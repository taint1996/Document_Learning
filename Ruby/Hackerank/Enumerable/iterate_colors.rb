# In this challenge,
# you have been provided with a custom object called colors that defines its own each method.
# You need to iterate over the items and return an Array containing the values.

####### Use each #######
def iterate_color(colors)
  arr = []
  colors.each do |item|
    arr << item
  end
  arr
end

####### Another way use select #######
def iterate_color(colors)
  colors.select { |obj| obj }
end

####### Iterate color by map #######
def iterate_color(colors)
  colors.map { |item| item }
end
