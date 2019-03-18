def devisors(n)
    divisors = (2..n).select( |number| n % number == 0)
    divisors.length == 0 ? "#{n} is prime" : divisors
end 