# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.
def find_short(s)
    # your code here
    split_strings = s.split()
    l = split_strings.sort_by(&:length)
    return l[0].length # l: length of the shortest word
end
find_short("123 a abc xy xyz")