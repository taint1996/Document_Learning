# Complete the following Python program to compute the sum
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 recursively

# for loop
def sum_by_loop():
  s = 0
  for i in range(11):
    s = s + i
  return s

# with recursive
def sum(n):
  if n <= 1:
    return n
  else:
    return n + sum(n - 1)
