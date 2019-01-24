# TryRuby
books = {} # Create a hash Books
books["Gravitys Rainbow"] = :sqlendid
books["The deep end"]  = :abyssmal
books["Living colors"] = :mediocre

print "Books: ", books
print "\n"

puts books.length

puts books.keys # return keys books

ratings = Hash.new {0}

books.values.each { |rate|
  ratings[rate] += 1
}
print "Rating: #{ratings}\n"
