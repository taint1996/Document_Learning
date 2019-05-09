### Example 1
def call_block 
	puts "Start of method"
	yield 
	puts "End of method"
end

call_block do 
	puts "I'm inside call_block method"
end

####### Example 2
def calculate(a,b)
    yield(a, b)
end

puts calculate(15, 10) {|a, b| a - b}

##### Example 3
def factorial(n)
	result = (1..n).reduce(&:*)
	yield result
end 

n = gets.to_i
factorial(n) do |result|
	puts result
end

##### Example 5
def add(a, b)
	yield(a,b)
end

add(1, 2) { |a, b| a + b }

##### Example 5
def file_open_write(name)
	begin 
		f = File.open(name, "w")
		yield f
	ensure 
		f.close
	end
end

file_open_write("test.txt") do |f| 
	f.puts "Write something zzz"
end
