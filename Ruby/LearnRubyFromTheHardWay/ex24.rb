puts "Let's practice everything"
puts 'You\'d need to know \'bout escape with \\ that do \n newlines and  \t tabs.'

poem = <<END
  \tThe lovely world
with logic so firmly planted
cannot discern \t the needs of love
not comprehend passion from intuision 
and requires an explanation
\n\t\t where there is none
END

poem2 = <<BIGDOC
  \tThe lovely world
with logic so firmly planted
cannot discern \t the needs of love
not comprehend passion from intuision 
and requires an explanation
\n\t\t where there is none
<<BIGDOC

puts "-----------------"
puts poem
puts "-----------------"

five = 10 - 2 + 3 - 6
puts "This should be five #{five}"

def secret_fomular(started)
  jelly_beans = started * 500
  jars = jelly_beans / 1000
  crates = jars / 100
  return jelly_beans, jars, crates
end

start_point = 1000
beans, jars, crates = secret_fomular(start_point)

puts "With a starting point of: #{start_point}"
puts "We'd have #{beans} beans, #{jars} jars, and #{crates} crates"

start_point = start_point / 10

puts "We can also do that this way:"
puts "We would have %s beans, %d jars, and %d crates." % secret_fomular(start_point)