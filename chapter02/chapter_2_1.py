# -*- coding: utf-8 -*-
__author__ = 'kiwi'

# This is the begining of my learning from Python :)
print('''123 Let us go!''')  # ? why we cannot use double quote marks here
print("J'aime %s" % 'Xqq')
birthday_month = 'december'  # the month of the birthday month
print('my birthday is in %s' % birthday_month)
# the underscores(_) can be the first character in a variable name
_underscore = '_'
print('''this is underscore, %s''' % _underscore)
legalBabyName = 'Meow '  # cambelCase for variable name
print ('Cat', 1)
dollars = 6
print '1 RMB exnchanges to Canadian dollars is ', dollars, 'before'
dollars = 4.99  # no currency symbol in the value
print 'but now is', dollars, '- _ -|||'
# page 47
print type(dollars)
print type(1)  # ?  why it shows <class'int'> in the book

'''
check point
2.10. the variable is the piece of data with a name to store the memory
2.11
    legal
    illegal
    legal
    legal
    illegal
    legal
2.12 diff. because S is upper case and s is lower case which is recognize as different element of string here
2.13 invalid. The first letter of name fo variable cannot be integer
2.14 the value is val
2.15
    int
    float
    float
    int
    str
2.16 0
'''
opening = int(input('Bonjour! Please enter anything here: '))  # input(promp) a string displays on the screen
#? cannot display a string , why ????

print 'The variable is: ', opening

dollars_int = int(dollars)  # dollars has already asisgned above
print dollars_int
dollars_float = float(dollars_int)
print dollars_float