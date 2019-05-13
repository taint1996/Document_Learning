# . Let's say you have a list of 100 integers and you want to group them according to their even and odd value.
  ood_number = (1..100).group_by(&:odd?)
  even_number = (1..100).group_by(&:even?)
# refactor
number = (1..100).group_by { |x| x % 2 }


#### In this challenge, your task is to group the students into two categories corresponding to their marks obtained in a test. The list of students will be provided in a marks hash with student name as key and marks obtained (out of 100) as value pair, along with the pass_marks as argument.
# Example
# > marks = {"Ramesh":23, "Vivek":40, "Harsh":88, "Mohammad":60}
# > group_by_marks(marks, 30)
# => {"Failed"=>[["Ramesh", 23]], "Passed"=>[["Vivek", 40], ["Harsh", 88], ["Mohammad", 60]]}
def group_by_marks(marks, pass_marks) 
  marks.group_by do |key, value|
    (value > pass_marks) ? "Passed" : "Failed"
  end
end