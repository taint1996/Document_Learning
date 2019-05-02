require 'json'
require 'stringio'

def counting_valleys(n, s)
s.split.map do |words|
words.chars.each_with_index do |v, idx|
case v 
when "U"
	"/" 
when "D"
	"\\\n"
else 
	"_"
end
end 
end 
end 

fptr = File.open(ENV['OUTPUT_PATH'], 'w') 

n = gets.to_i 
s = gets.to_s.rstrip

result = counting_valleys(n, s) 

fptr.write result 
fptr.write "\n"
fptr.close()