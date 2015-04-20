# -*- coding: utf-8 -*-
__author__ = 'kiwi'
print 'chapter10'


def dictionary():
    phonebook = dict()
    print phonebook
    phonebook.clear()
    phonebook.keys()
    phonebook.get('id', 'Entry not found')
    phonebook.pop('id', 'Entry not found')
    phonebook.items()  # return tuples, empty dictionary return keyError

# dictionary()

'''？？？
pop Returns the value associated with a specified key and removes
that key-value pair from the dictionary. If the key is not found,
the method returns a default value.
'''

'''
page 394 checkpoint
10.1    value and key
10.2    key
10.3    'start' is the key and 1472 is the value
10.4    store the pair of key-value in the dictionary of employee
10.5 ccc
10.6    search the key-value pair by input the key for the output of value, if keyError or value is not exist,
then it does not exits
10.7    delete the key-value of 654 as the key in the inventory dictionary
10.8 3
10.9 (1 , 'aaa'), (2 , 'bbb'), (3 , 'ccc')
10.10   pop is delete the key or value you enteres, the opoitems delete the whole pair
10.11 the key-value pair as tuple
10.12   list of key
10.13 list of value
'''


def set_section():
    a_set = set()
    two_set = set()
    a_set.add(34)
    a_set.add('swe')
    a_set.update([1, 2, 3])
    print a_set
    two_set.update([3, 4, 5])  # [2,3,4,5]
    print two_set
    set3 = a_set.union(two_set)
    print set3
    for var in a_set:
        print 'loop', var
    a_set.remove(3) #remove method raises a KeyError exception
    print a_set
    a_set.discard(2)    # remove but don't raise exception
    print a_set
    a_set.clear()   # clear all the value
    print a_set


'''???
does'not display the way that page 397 :{1, 2, 3, 8, 9, 10}
'''
set_section()

# page 399 bottom the statement in line 3

















