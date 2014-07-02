'''
Created on Jul 2, 2014

@author: viejoemer

How to create a dictionary in Python?

¿Cómo crear un diccionario en Python?

A dictionary is mutable and is another container type that can 
store any number of Python objects, including other container 
types.
'''

#dict empty {}
d = {}
print(d)

#dict empty with the method dict()
d = dict()
print(d)

#dict with values using the method dict()
d = dict(one=1, two=2, three=3)
print(d)

#dict with values using {}
d = {"one":1, "two":2, "three":3}
print(d)

#dict with zip and dict methods
d = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(d)

#creating a dict using list and tuples
d = dict([('two', 2), ('one', 1), ('three', 3)])
print(d)

#Creating a dict using {} and method dict()
d = dict({'three': 3, 'one': 1, 'two': 2})


