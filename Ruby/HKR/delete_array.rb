arr = [5, 6, 5, 4, 3, 1, 2, 5, 4, 3, 3, 3]

p arr.pop(3) # [5, 6, 5, 4, 3, 1, 2, 5, 4] -> delete 3 element from the end of array

p arr.shift # delete an element from begin of array

p arr.delete_at(2) # delete an element at a given position 

p arr.delete(5) # [6, 4, 3, 1, 2, 4, 3, 3, 3] -> Delete all occurrences of a given element

def end_arr_delete(arr)
    # delete the element from the end of the array and return the deleted element
    arr.pop
end

def start_arr_delete(arr)
    # delete the element at the beginning of the array and return the deleted element
    arr.shift
end

def delete_at_arr(arr, index)
    # delete the element at the position #index
    arr.delete_at(index)
end

def delete_all(arr, val)
    # delete all the elements of the array where element = val
    arr.delete(val)
end