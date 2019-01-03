import sys

print(sys.executable)
print(sys.version)


class Employee:
  def __init__(self, first, last):
    self.first = first
    self.last = last

  @property
  def email(self):
    return '{}.{}@gmail.com'.format(self.first, self.last)

  @property
  def fullname(self):
    return '{} {}'.format(self.first, self.last)


for num in [1, 2, 3, 4]
  print(num)

employ1 = Employee('Beo', 'Ka')

print(employ1.first)
print(employ1.email)
print(employ1.fullname)
