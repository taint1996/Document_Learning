# Initialize 3 variables here as explained in the problem statement
empty_hash = Hash.new

default_hash = Hash.new(1)

hackerrank = {"simmy" => 100, "vivmbbs" => 200}

user = {"viv": 10, "simmy": 20, "sp2hari": 30}
user.each { |key, value| puts "#{key} - #{value}"}

def iter_hash(hash)
	# hash.each { |key, value| puts "#{key}\n#{value}"}
	hash.each { |key| puts key }
end

######################## Ruby Hash - Addition, Deletion, Selection ########################
# initialize a hash
h = Hash.new
h.default = 0 # -> {}

h["abc"] = 1 # -> {"abc": 1}
	# or
h.store("abcd", 2) # -> {"abc" => 1, "abcd" => 2}

h.delete("abc") # delete key "abc" in h

hackerrank = Hash.new
hackerrank[543121] = 100

hackerrank.keep_if { |key, value| key.is_a? Integer }
hackerrank.delete_if { |key, value| key.even? }

