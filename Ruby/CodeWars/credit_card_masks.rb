# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question 
# is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. 
# Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into '#'.

def maskify(input)
    # 6546546546564665 to "############# 4665"
    array = input.to_s.split(//).reverse!
    flipped_array = []

    if array.length > 4
        array.each_with_index { |element, index|
            if index <= 3
                flipped_array << element 
            else
                flipped_array << "#"
            end            
        }
        flipped_array.reverse!
        print flipped_array.map! { |item| "#{item}" }.join()
    else
        puts input.to_s
    end
end 

## Alternative
def maskify(cc)
    # 6546546546564665 to "############# 4665"
    cc.length < 4 ? cc : "#" * (cc.length - 4) + cc[-4..-1]
end

