# reduce
# Task sum term which terms(n) = n^2 + n + 1, n >= 0
def sum_term n
  (1..n).reduce(0) { |acc, curr| acc += (curr ** 2 + curr + 1)}
end

############################# any
arr = [1, 2, 3, 4, 5, 6] # => [1, 2, 3, 4, 5, 6]
arr.any? {|a| a % 2 == 0} # => True. checks if any number in the array is even
h = {"a" => 1, "b" => 2, "c" => 3} # => {"a" => 1, "b" => 2, "c" => 3
h.any? { |key, value| value.is_a? String} # => False

############################# all 
arr.all? { |item| item.is_a? Integer } # => checks if all elements of the array are of the type Integer
# => True

h.all? { |key, value| key.is_a? String } # True

############################# none 
# Checks if none of the elements in the array are of nil type
arr.none? { |i| item.nil? } # => True
h.none? {|key, value| value < 3} # checks if all values of the Hash object are less than 3
# => False

############################# find
 # returns the first element greater than 5 and `nil` if none satisfies the condition
arr.find { |x| x > 5 } # => 6

def func_any(hash)
    # Check and return true if any key object within the hash is of the type Integer
    # If not found, return false.
    hash.any? { |key, value| key.is_a?(Integer) }
end

def func_all(hash)
    # Check and return true if all the values within the hash are Integers and are < 10
    # If not all values satisfy this, return false.
    hash.all? { |key, value| value.is_a?(Integer) && value < 10 }
end

def func_none(hash)
    # Check and return true if none of the values within the hash are nil
    # If any value contains nil, return false.
    hash.none? { |key, value| value.nil? }
end

def func_find(hash)
    # Check and return the first object that satisfies either of the following properties:
    #   1. There is a [key, value] pair where the key and value are both Integers and the value is < 20     
    #   2. There is a [key, value] pair where the key and value are both Strings and the value starts with `a`.
    hash.find do |k, v| 
      (k.is_a?(Integer) && v.is_a?(Integer) && v < 20) || 
      (k.is_a?(String) && v.is_a?(String) && v.start_with?('a'))
    end
end
