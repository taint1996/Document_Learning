# Write a Ruby program to check if a string starts with "if".
def start_if(str)  
  return str[0, 2] == "if"
end

puts start_if("ifelse")
puts start_if("hello")