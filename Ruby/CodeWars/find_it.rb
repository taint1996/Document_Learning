# Given an array, find the int that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.
def find_it(seq)
	seq.detect { |n| seq.count(n).odd? }
end

def find_it(seq)
	seq.each_index do |idx| 
	    if seq.count(seq[idx]).odd?
	      return seq[idx]
	    end
	 end
end 