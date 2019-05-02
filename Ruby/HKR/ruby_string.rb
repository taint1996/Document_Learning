# Text info can be read from varied sources and is often unsuitable for direct processing or usage by core functions. 
# This necessitates methods for post-processing and data-fixing. 
# In this tutorial, we'll learn how to remove flanking whitespace and newline from strings.

# String.chomp(separator=$/): Returns a new string with the given separator removed from the end of the string (if present). 
	# If $/ has not been changed from the default Ruby record separator, 
	# then chomp also removes carriage return characters (that is, it will remove \n, \r, and \r\n).
"Hello World!  \r\n".chomp # -> "Hello World!  "
"Hello World!".chomp("orld!") -> "Hello W"
"Hello W"
"hello \n there".chomp
"hello \n there"

# String.strip - Returns a new string with the leading and trailing whitespace removed.
"           string  ".strip # -> "string"

# String.chop - Returns a new string with the last character removed. 
	# Note that carriage returns (\n, \r\n) are treated as single character and, 
	# in the case they are not present, a character from the string will be removed.
"string\n".chop # "string"
"string".chop # "strin"

def process_text(arr)
    arr.map(&:strip).join(' ')
end 

########################################## Ruby string iteration ##########################################
def count_multibyte_char(str)
    str.each_char.select { |x| x if x.bytesize() > 1 }.count
end

########################################## Ruby String Indexing ##########################################

# Task: '002-10.00-20.00' to '002-15.00'
def serial_average(str)
    "#{str[0,4]}#{format('%.2f', ((str[4,5].to_f + str[10,5].to_f)/2).round(2))}"
end 


arr = [5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5]
b = arr.group_by { |x| x }.reduce(0) do |acc, curr|
s = curr[1].length
if s / 2 != 0
	acc += s / 2
end
end
