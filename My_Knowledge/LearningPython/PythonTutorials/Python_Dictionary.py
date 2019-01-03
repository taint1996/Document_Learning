import Sort_Python as sort_py

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
# Write a Python script to add a key to a dictionary
def ex2():
    dict = {0: 10, 1: 20}
    dict1 = {2: 30}

    dict.update(dict1)
    return dict

# Write a Python script to concatenate following dictionaries to create a new one.
def ex3():
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50, 6:60}
    dict4 = {}

    for d in (dic1, dic2, dic3):
        dict4.update(d)

    x = 4
    if x in dict4:
        print("%s is present in dict" % x)
    else:
        print("Value %s" + x + " is empty")
    return dict4

# Write a Python program to iterate over dictionaries using for loops
def ex4():
    d = {'x': 10, 'y': 20, 'z': 30}

    for dict_key, dict_value in d.items():
        print(dict_key, " -> ", dict_value)

    return dict_key,dict_value

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
def ex6():
    n = int(input("Enter a number: "))
    d = dict()

    for x in range(1, n + 1):
        d[x] = x * x

    return d

# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
def ex7():
    n = int(input("Enter a Number: "))

    d = {}

    for x in range(1, n + 1):
        d[x] = x ** 2
    return d

# Write a Python script to merge two Python dictionaries
def ex8():
    d1 = {'a': 100, 'b': 200}
    d2 = {'x': 300, 'y': 400}

    d = d1.copy() # insert d1 to d
    d.update(d2)
    return d

# Write a Python program to sum all the items in a dictionary
def sum_dictionary():
    my_dict = {'a': 100, 'b': 200, 'x': 300, 'y': 400}
    return sum(my_dict.values())

# Write a Python program to multiply all the items in a dictionary.
def multiply():
    my_dict = { 'a': 100, 'b': 200, 'x': 300, 'y': 400 }

    res = 1

    for x in my_dict:
        res *= my_dict[x]
    return res

# Write a Python program to remove a key from a dictionary.
def remove_key():
    my_dict = { 'a': 100, 'b': 200, 'x': 300, 'y': 400 }

    if 'a' in my_dict:
        del my_dict['a']
    else:
        print("There is not have a key you want to remove")
    return my_dict

 # Write a Python program to map two lists into a dictionary.
def map_list_to_dict():
    keys = ['red', 'green', 'blue']
    values = ['#FF0000','#008000', '#0000FF']

    combine = dict(zip(keys, values))
    print("Map List to Dictionary: %s" % combine)

# Write a Python program to sort a dictionary by key.
def sort_dict():
    color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}
    for key in sorted(color_dict):
        print("Sort Dict %s %s" % (key, color_dict[key]))

# Write a Python program to get the maximum and minimum value in a dictionary.
def compare_max_min_dict():
    my_dict = {'x':500, 'y':5874, 'z': 560, 'a': 2000, 'b': 100, 'c': 400}

    key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
    print("Maximum Key: ", my_dict[key_max])

    key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
    print("Minimum Key: ", my_dict[key_min])

# Write a Python program to get a dictionary from an object's fields.
class dictObj(object):
    def __init__(self):
        self.x = "red"
        self.y = "green"
        self.z = "blue"
test = dictObj()
print("Get a dictionary from an object's fields: %s" % test.__dict__)

# Write a Python program to remove duplicates from Dictionary.
def remove_duplicate_from_dict():
    student_data = {'id1':
       {'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
       },
     'id2':
      {'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
       },
     'id3':
        {'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
       },
     'id4':
       {'name': ['Surya'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
       },
    }

    result = {} # or result = dict()
    for key, value in student_data.items():
        if value not in result.values():
            result[key] = value
    return result


# Write a Python program to check a dictionary is empty or not.
def check_present_dict():
    my_dict = {}

    if not bool(my_dict):
        print("Dictionary is Empty")

# Write a Python program to combine two dictionary adding values for common keys
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
def combine_adding_values_dict():
    d1 = {'a': 100, 'b': 200, 'c':300}
    d2 = {'a': 300, 'b': 200, 'd':400}
    from collections import Counter
    d3 = Counter(d1) + Counter(d2)
    print("Combine Adding Value in Dict: ", d3)

if __name__ == '__main__':
    exam1 = ['e', 'a', 'u', 'o', 'i']
    sort_py.ex1(exam1)
    # Example 2
    print("Dictionary Ex2: %s" % ex2())
    print("Concat Dictionary: %s " % ex3())
    ex4()

    # print("Generate a dict contain a number in (x, x*x): %s " % ex6())
    # print("Generate a dict contain a square of keys: %s " % ex7())
    print("merge two Python dictionaries: %s" % ex8())
    print("Sum all values in Dict: %s" % sum_dictionary())
    print("Multiply all values in Dict: %s" % multiply())
    print("Remove a key in Dict: %s" % remove_key())

    map_list_to_dict()
    sort_dict()
    compare_max_min_dict()
    check_present_dict()

    combine_adding_values_dict()
