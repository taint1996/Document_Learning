# Write a Ruby program to accept a filename from the user print the extension of that.
file = "/abc/xyz/ruby.rb"
fileName = File.basename file # file name: ruby.rb
baseName = File.basename file, ".rb" # base name: ruby
extension = File.extname file # extension: .rb
pathName = File.dirname file # path name: abc/xyz
puts "filleName: #{fileName}"
puts "base name: #{baseName}"
puts "extension: #{extension}"
puts "pathName: #{pathName}"