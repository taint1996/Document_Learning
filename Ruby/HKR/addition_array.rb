x = [1, 2]

# push allows one to add an element to the end of the list.
x.push(3,4) # -> [1,2,3,4]

# insert allows one to add one or more elements starting from a given index (shifting elements after the given index in the process)
x.insert(0,1,2,3,4) # -> [1,2,3,4,1,2] 0: position to insert

# unshift allows one or more elements to be added at the beginning of the list.
x.unshift(1,2,3) # -> [1,2,3,1,2]

def end_to_add(arr, element) 
	arr.push(element)
end

def begin_arr_add(arr, element)
	arr.unshift(element)
end

def index_arr_add(arr, index, element)
	arr.insert(index, element)
end 

def index_arr_multiple_add(arr, index)
    # add any two elements to the arr at the index
    arr.insert(index, index + 1, index + 2)
end