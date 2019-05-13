# String data types are a sequence of characters, each of which occupies 1 byte of memory. 
# Technically, you could represent the string using an array (or some collection) of characters, similar to that of classic languages like C

# Single quoted strings 
# The easiest way of adding text is by surrounding it with single quote (apostrophe) symbols. However, characters like an apostrophe and a backslash within the string need to be escaped if they are present.
'Hello! Programmer. How\'s it going?'

# Double quoted String
# Double quoted strings are more flexible, and they allow special escape sequences, e.g.\t, \n, 
# which don't work with single quoted strings. More importantly, they allow the embedding of arbitrary expressions
"My name is Circle, and I love Pi. Pi is equal to #{Math::PI}"

document = <<-HERE         # We begin with <<- followed by the ending delimiter HERE
This is a string literal.
It has two lines and abruptly ends with a newline...
HERE

def single_quote
  # single quote string here
    'This is a single quote. How\'s it work?'
end

def double_quote
  # Double quote string here
    "this is double squote \t\n single can not do this. Haha"
end

def here_doc
  # Here doc string here
    <<-EOF
    Here doc string here
    EOF
end