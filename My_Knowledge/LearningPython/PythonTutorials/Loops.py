####### For Loops
workingDay = [2,3,4,5,6]

for day in workingDay:
  print(day)

for item in range(1, 10, 2):
  print (item) # => 1 3 5 7 9

###### While Loops
x = 0
while (x <= 5):
  print("X: ", x)
  x += 1

### Else clause in while loops
x1 = 5

while x1 <= 10:
  print(x1)
  x1 += 1
else:
  print("Inside Else")

n = 0
for n in range(5):
  n += 1

  if n == 3:
    continue
  print(n)

