require 'json'
require 'stringio'

# Complete the sockMerchant function below.
def sockMerchant(n, ar)    
    ar.group_by { |x| x }.reduce(0) do |acc, curr|        
        s = (curr[1].length % 2 != 0) ? (curr[1].length - 1) : curr[1].length
        if (s % 2 == 0)
            acc += (s / 2)
        end
    end
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

n = gets.to_i

ar = gets.rstrip.split(' ').map(&:to_i)

result = sockMerchant n, ar

fptr.write result
fptr.write "\n"

fptr.close()