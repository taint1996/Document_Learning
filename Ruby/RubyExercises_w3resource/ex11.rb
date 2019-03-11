# Write a Ruby program to print the following 'here document'.

# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

HERE_DOCUMENT = %q(
  Sample string: 
  a string that you "dont" have to escase
  This
  is a ......... multi-line
  heredoc string --------> example
)
puts "Here document" + HERE_DOCUMENT

secondWay = (
  <<-eos 
  Sample string: 
  a string that you "dont" have to escase
  This
  is a ......... multi-line
  heredoc string --------> example
  eos
)
puts secondWay
