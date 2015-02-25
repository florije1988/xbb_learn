# -*- coding: utf-8 -*-
__author__ = 'kiwi'
print 'chapter10'
def dictionary():
    phonebook = dict()
    print phonebook
    phonebook.clear()
    phonebook.keys()
    phonebook.get('id','Entry not found')
    phonebook.pop('id','Entry not found')
    phonebook.items()   # return tuples, empty dictionary return keyError

dictionary()

'''？？？
pop Returns the value associated with a specified key and removes
that key-value pair from the dictionary. If the key is not found,
the method returns a default value.
'''

'''
page 394 checkpoint
10.1
10.2

'''