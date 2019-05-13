colors = ['red', 'green', 'blue']
colors.each_with_index { |item, idx| p "#{idx} - #{item}" }

##### Solution
animals = ['leopard', 'bear', 'fox', 'wolf']
def skip_animals(animals, skip)
  animals.map.with_index{|item, index| "#{index}:#{item}" if index >= skip}.compact
end
