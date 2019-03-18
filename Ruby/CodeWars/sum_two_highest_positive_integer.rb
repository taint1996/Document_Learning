# Create a function that returns the sum of the two lowest positive numbers given an array of maximum 4 integers. No floats or empty arrays will be passed.
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 42 + 77.
def sum_two_highest_positive_integers(numbers)
    sorted = numbers.sort!
    sorted[-1] + sorted[-2]
end

# Alternative 1
def sum_two_highest_positive_integers(numbers)
    numbers.sort![0..1].inject(:+)
end

def sum_two_highest_positive_integers(numbers)
    numbers.min(2).reduce(:+)
end