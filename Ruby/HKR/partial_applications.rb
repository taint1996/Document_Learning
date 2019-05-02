multiply_function = -> (number) do 
	-> (another_number) do 
		number * another_number
	end 
end

doubler = multiply_function.(2)
tripler = multiply_function.(3)

puts doubler.(4)
puts tripler.(3)


# Here, combination is a variable that stores a partial application which computes combination nCr.
combination = -> (n) do
    -> (another_number) do 
        (n - another_number + 1..n).inject(&:*) / (1..another_number).inject(&:*)
    end 
end 

n = gets.to_i
r = gets.to_i
nCr = combination.(n)
puts nCr.(r)
