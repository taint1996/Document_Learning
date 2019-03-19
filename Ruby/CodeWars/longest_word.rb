def find_long_word(s)
    split_strings = s.split()
    l = split_strings.sort_by(&:length).reverse!
    return l[0].length
end 
find_long_word("1 123 4444 555 5 123123 abcdxyz aaaa")