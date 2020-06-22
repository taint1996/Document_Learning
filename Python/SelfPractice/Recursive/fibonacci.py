# Starting at 0 or 1
  # for n > 1:
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fib_w_loop(num):
  a,b = 0, 1
  while b <= num:
    a, b = b, a + b
  return a

# recursive
def fibonacci_recursive(num, a, b):
  if b >= num:
    return b
  else:
    return fibonacci_recursive(num, b, a+b)

