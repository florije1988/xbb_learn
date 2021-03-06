# -*- coding: utf-8 -*-
__author__ = 'kiwi'

print 'Chapter 11 Classes and Object-Oriented Programming'
'''
two methods of programming: procedures and object-oriented
An object's methods are functions that perform operations on the object's data attributes
Encapsulation refers to the combining of data and code into a single object
data hiding refers to an object's ability to hide its data attributes from code that is outside the object

page 424
checkpoint
11.1 the object is the several functions perform an operation on the object's data
11.2 The encapsulation is the combining the data and code into a single object
11.3 The reason why an object's internal data usually hidden from outside code is because the process and internal
data does not needs to display on the display
11.4   The public methods is public working, external(entities) object; the private methods is the private working, internal object

A class is code that specifies the data attributes and methods for a particular type of object
The 'self' parameter is required in every method of a input_class
The __init__ method is commonly known as an initializer methods

'''

import random


class coin_flip:
    def __init__(self):
        self.sideup = 'heads'

    # ??? does self.sideup just a variable ???
    def toss(self):
        coin = random.randint(0, 1)
        if coin == 0:
            self.sideup = 'tails'
        return self.sideup

    def get_sideup(self):
        return self.sideup


def main():
    my_coin = coin_flip()  # an object is created in memory from the coin_flip input_class, __init__ is executes
    print 'the side is up: %s' % my_coin.get_sideup()
    print 'tossing '
    my_coin.toss()
    print 'The side is: %s' % my_coin.get_sideup()

# main()

'''
Hiding attributes
executing the data and the calculation internal

1. set up the doc as : name.py
2. set up input_class content in the name.py
3. import the file into another file by
    'import name /n name.content() # name.content() is the object as same as the my coin above'

The __str__ methods is also called automatically when an object is passeed as an argument to the built-in str
function.

checkpoint (page 442)
11.5    The blueprint represent the object
11.6    In this chapter, we use the metaphor of a cookie cutter and cookies that are made from the cookie to describe
classes and objects. In this metaphor are objects the cookie cutter
11.7    the automatically running when the class was called.
11.8    The purpose of the self parameter in a method that helps the function was run in the calling of the class
11.9    In a python input_class, use the import to hide an attribute from code outside the input_class
11.10   the purpose of the __str__method is for displaying
11.11   The __str__ methods is also called automatically when an object is passeed as an argument to the built-in str
function.


Definition:
Instances Attributes: A method uses the self parameter to create an attribute and the attributes belongs to the specific
object (self references)
Accessor method: a method returns a value from a input_class's attribute but does not change
Mutator method: A method that stores a value in a data attribute or changes the value of a data attribute in some other way
It can control the way that a input_class's data attributes are modified
Mutator methods also calls setters and accesors methods are called getters


page 456
'''

import input_class


def main():
    flip_coin = input_class.coin().flip_times(int(raw_input('Please input raw times: ')))
    for i in range(len(flip_coin)):
        print flip_coin[i]
    return True

# main()













