# Python Oject Oriented Programming

class Employee:
  raise_amt = 1.04
  num_of_emps = 0

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@gmail.com'

    Employee.num_of_emps += 1

  def fullname(self):
    return '{} {}'.format(emp1.first, emp1.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amt)

  @classmethod
  def set_raise_amt(cls, amount):
    cls.raise_amt = amount

  def from_string(cls, emp_str):
    first, last, pay = emp_str.split('-')
    return cls(first, last, pay)

emp_str_1 = 'BeoKa-Kun-3000'

new_emp_str = Employee.from_string(emp_str_1)
print(new_emp_str.email)

# Employee.set_raise_amt(2)

# emp1 = Employee('Beo', 'Ka', 20000)

# print(Employee.fullname(emp1))
# print(emp1.pay)

# print(emp1.__dict__)
