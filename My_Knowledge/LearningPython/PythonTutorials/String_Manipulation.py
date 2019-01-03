str = "Hello World!"
print(str[0]) # H
print(str[7]) # W
print(str[0:5]) # Hello
print(str[6:12]) # World!

print(str[6:-1]) # World

####### Reverse a string
str1 = "Python String"
print(str1[::-1])
print(str1[0:12:3]) # string[begin:end:step]


########## len() method
str2 = "Hi Am Beo Ka ^^"
print(len(str2))
substr = "Object"
print(str.count(substr)) # return 0 because substr not in str2

############# index() method
#index(substr, start, end)
str = "Python is Object Oriented"
substr = "is"
print(str.index(substr))


## Upper and Lower case
print(str.upper())
print(str.lower())

# startswith()/ endswith() method
print(str.startswith('Python'))
print(str.endswith('Python'))

# split() method
print(str.split())

str1 = 'Python,is,Object,Oriented'
sList = str1.split(',')
for temp in sList:
  print(temp)

