arr = [1, 2, 3, 4, 56, 6, 7, 8]

def simpleOfArray(ar)
	s = 0

	ar.each_with_index { |x| s += x }
	s # return x
end

print(simpleOfArray(arr))

def simpleOfArray1(ar)
	s = 0

	ar.each do |x|
		s += x
	end
	s # return x
end
print("\nSum of Array 1: ", simpleOfArray(arr))

def simpleOfArray2(ar)
	ar.inject(&:+)
end
print("\nSum of Array 2: ", simpleOfArray(arr))

def sum(numbers)
  if numbers.empty?
  	
  else
    first, *rest = numbers
    first + sum(rest)
  end
end
print("\nSum: ", sum(arr))

# Để tạo ra một thuật toán linh hoạt hơn, 
# và để tối ưu hóa nó cho việc sử dụng đệ quy, 
# chúng ta sử dụng một giá trị khởi đầu, và sẽ gọi nó là accumulator.
def sum1(accumulator, numbers)
  if numbers.empty?
    accumulator
  else
    first, *rest = numbers
    sum(accumulator + first, rest)
  end
end
print("\n Sum by accumulator: ", sum1(20, arr))




