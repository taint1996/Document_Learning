# String.include?(string) - Returns true if str contains the given string or character.
"string".include? "ng" # return true
"string".include? "gn" # return false

# String.gsub(pattern, <hash|replacement>) - Returns a new string 
  # with all the occurrences of the pattern substituted for the second argument: . 
  # The pattern is typically a Regexp, but a string can also be used.
"hello".gsub(/[aeiou]/, '*') # h*ll*
"hello".gsub(/[aeiou]/, '') # hll

# In this challenge, your task is to write the following methods:

# mask_article which appends strike tags around certain words in a text. 
# The method takes 2 arguments: A string and an array of words. 
# It then replaces all the instances of words in the text with the modified version.
# A helper method strike, given one string, appends strike off HTML tags around it. 
# The strike off HTML tag is <strike></strike>.

def mask_article(string, words)
  words.each { |x| string.gsub!(x, strike(x))}
  string
end

def strike string
  "<strike>#{string}</strike>"
end