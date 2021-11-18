# Author: Yves du Toit
#!/usr/bin/python

# you generally import and modules or methods above the main clause
# import os
import random
from my_module.my_python_functions import add, add_print


# you generally declare functions and classes above the main clause
def tester():
    return "tester"

# the main clause
# this is where the body of the program exists
if __name__ == "__main__":
    
    # int declaration 
    # any non decimal number
    # we can perform mathematical operations on numbers
    int_example = 1
    speed = 34.5
    
    # float declaration
    # any number with a decimal floating point
    # we can perform mathematical operations on floats as well
    float_example = 1.00
    
    # python indexing starts at 0

    # string declaration
    # any alpha-numerical character within a set of ""
    # is iterable
    string_example = str()
    char_string_word = "sdfklsdjfgs1231"
    char_1 = "123"
    char_2 = "456"
    # we can concatanate strings using the + operator
    char_3 = char_1 + char_2 + "any string as well" + "789" + str(10)

    # list also known as arrays or matrices declaration
    # lists are ordered and are therefore hashable
    # lists allow any data type to be stored
    # lists allow duplicate values
    
    list_example = []
    list_example_2 = list()

    list_example_1 = [1,2,3]
    # adding to a list
    list_example_1.append(4)

    
    list_example_2.append(1)
    list_example_2.append(2)
    list_example_2.append(3)

    # removing from a list by index
    list_example_2.pop(2)
    print(list_example_2)

    # set declaration
    # sets are unordered and are therefore not hashable
    # sets only allow unique values, will overide the first observation when subsequent same observations are entered
    set_example_1 = set()
    set_example_2 = {}
    
    # dictionary declaration
    # dictionaries store key: value pairs
    # dictionaries are ordered by key
    # dictionaries can have any hashable data type as a key
    # a dictionary key can have any data type as a value
    dictionary_example = {"key": "value", "key_2": "value_2"}
    dictionary_example_1 = dict()

    # retrieving a dictionary value
    print(dictionary_example["key_2"])

    # special dictionary methods 
    # keys returned as a list
    dict_keys = dictionary_example.keys()

    # values returned as a list
    dict_values = dictionary_example.values()

    # key, value pairs as a tuple
    dict_items = dictionary_example.items()

    print()
    print("iterating over dictionary key value pairs")
    for key, value in dictionary_example.items():
        print(key, value)

    # tuple declaration
    # tuples are like lists except they are not indexable
    tuple_example = (1,2)

    # if else conditionals
    if speed >= 25.0:
        print("True 1")
    elif speed >=25.0 and speed <= 40.0 :
        print("True 2")
    elif speed >=25.0 or speed >= 40.0 :
        print("True 3")        
    elif speed >=20.0:
        print("True 4")
    else:
        print("else")
    
    # loops
    # works for any iterable type
    iterable = [1,2,3,4]

    print()
    for value in iterable:
        print(value)

    print()
    for value in [1,2,3,4]:
        print(value)
        print(value + 1)


    print()
    for value in "abcde":
        print(value)


    # enumerate creates an index variable 
    print()
    for index, value in enumerate(iterable, start=0):
        print(index, value)

    # list comprehension
    # comprehensions extend over all data types
    a_list_of_four = [1,2,3,4]
    # list comprehension
    a_list_of_four_doubled = [val + val for val in [1,2,3,4]]
    print()
    print(a_list_of_four_doubled)
    # set comprehension
    a_set_of_four_doubled = {val + val for val in {1,2,3,4}}
    print()
    print(a_set_of_four_doubled)
    # dict comprehension
    a_dict_of_four_doubled = {(key,val) for key,val in {"key_1": "value_1", "key_2": "value_2"}.items()}
    print()
    print(a_dict_of_four_doubled)

    my_rn = random.randint(1, 10)

    maths = add(num_1=10,
                num_2=5)

    add_print(num_1=10,
                num_2=5)