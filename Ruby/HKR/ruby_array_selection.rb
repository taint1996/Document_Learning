# The array class also allows to select and return a subset of an array based on some criteria defined in a block 
	# (a block is a group of code within {} that accepts a variable and returns a value).

# Selecting elements that satisfy a given criteria
# Rejecting elements that satisfy a given criteria
arr = [3, 4, 2, 1, 2, 3, 4, 5, 6]

arr.select { |x| x > 2 } # [3, 4, 3, 4, 5, 6]
arr.reject { |x| x > 2 } # [2, 1, 2]
arr.drop_while { |x| x > 1 } # [1,2,3,4,5,6] -- return element till the blocks returns false for the first time

# As you can see, the original array remains unchanged. This is called Non-Destructive Selection. 
# For destructive behavior (change to the original array), Ruby provides the following methods:

arr.delete_if { |x| x < 2 }
arr.keep_if { |x| x < 4 }

# For a destructive behavior for select and reject or any method that one wants to enforce a change in the original array, 
	# a ! can be used at the end of the method i.e., select! and reject!

def select_arr(arr)
  # select and return all odd numbers from the Array variable `arr`
    arr.select(&:odd?)
end

def reject_arr(arr)
  # reject all elements which are divisible by 3
    arr.reject { |x| x % 3 == 0 }
end

def delete_arr(arr)
  # delete all negative elements
    arr.delete_if { |x| x < 0 }
end

def keep_arr(arr)
  # keep all non negative elements ( >= 0)
    arr.keep_if { |x| x >= 0 }
end
