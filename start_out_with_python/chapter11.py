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
The 'self' parameter is required in every method of a class
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
    my_coin = coin_flip()   # an object is created in memory from the coin_flip class, __init__ is executes
    print 'the side is up: %s' % my_coin.get_sideup()
    print 'tossing '
    my_coin.toss()
    print 'The side is: %s'  % my_coin.get_sideup()

# main()

# page 432
