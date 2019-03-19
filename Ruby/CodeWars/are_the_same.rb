# Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, 
    # with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
# a = [121, 144, 19, 161, 19, 144, 19, 11]  
# b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]    

# a = [121, 144, 19, 161, 19, 144, 19, 11] 
# b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
def comp(array1, array2)
    array1.nil? || array2.nil? ? false : (array1.map { |item| item ** 2 }.sort! == array2.sort!)
end 

# Another Way
def comp(array, array2)
    array1 && array2 ? (array1.map { |item| item ** 2 }.sort! == array2.sort!) : false
end