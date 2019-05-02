multiply_numbers = -> (x, y) {
    x * y
}
p doublers = multiply_numbers.curry[2, 3]

power_number = -> (x, y) {
    x ** y
}
p power_number.curry[2,3]

######################################################### LAZY EVULATION #########################################################
### Lazy evaluation is an evaluation strategy that delays the assessment of an expression until its value is needed.
power_array = -> (power, array_size) {
	1.upto(Float::INFINITY).lazy.flat_map { |x| x ** power }.first(array_size)
}
p power_array[2, 5]


require 'prime'
n = gets.to_i 
p Prime.each.lazy.select { |x| x.prime? }.first(n)