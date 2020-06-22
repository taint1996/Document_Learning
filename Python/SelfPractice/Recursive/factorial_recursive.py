# n! = n x (n−1)!
# n! = n x (n−1) x (n−2)!
# n! = n x (n−1) x (n−2) x (n−3)!
# ⋅
# ⋅
# n! = n x (n−1) x (n−2) x (n−3) ⋅⋅⋅⋅ x 3!
# n! = n x (n−1) x (n−2) x (n−3) ⋅⋅⋅⋅ x 3 x 2!
# n! = n x (n−1) x (n−2) x (n−3) ⋅⋅⋅⋅ x 3 x 2

def factorial_recursive(n):
  if (n == 1):
    return 1
  else:
    return n * factorial_recursive(n - 1)