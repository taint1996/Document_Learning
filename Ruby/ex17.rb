# Exercise 17: More Files
from_file, to_file = ARGV

puts "Copying from #{from_file} to #{to_file}"

in_file = open(from_file)
indata = in_file.read

puts "The input file is #{indata.length}"

puts "Does the output file exist? #{File.exists?(to_file)}"
puts "Ready, hit Enter to continue, Ctrl-C to abort"

$stdin.gets

out_file = open(to_file, 'w')
out_file.write(indata)

puts "Alright, all done."
out_file.close
in_file.close
