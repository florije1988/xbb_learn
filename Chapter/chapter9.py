# -*- coding: utf-8 -*-
__author__ = 'kiwi'
print 'chapter9'

'''
page 348 checkpoint
9.1
input_word = raw_input('input word: ')
for i in input_word:
    print i
9.2 string[0]
9.3 9 or -1
9.4 indexError
9.5 len(string)
9.6 string has no effect
'''


def log_in():
    import login

    log_in_name = (raw_input('first_name: '))[:3]
    log_in_name += (raw_input('ast_name: '))[:3]
    log_in_name += (raw_input('id number: '))[-3:]
    return log_in_name


log_in()
'''
page 352 checkpoint
9.7 cde
9.8 defg
9.9 abc
9.10 abcdefg
'''


def test_string():
    input_string = raw_input('input string: ')
    for i in input_string:
        if input_string.isdigit() is True:
            print 'all are digits'
        elif input_string == 'q':
            print 'incldue q '
        elif 'like' not in input_string:
            print 'no like inside the string'

test_string()

#  isalnum(), isalpha(), isdigit(), islower(), isspace(), isupper()  <-- testing
# string.lower(), lstrip(), upper(),strip() <-- changing
'''???
page 356 lstrip() Returns a copy of the string with all leading whitespace characters removed.
Leading whitespace characters are spaces, newlines (\n), and tabs (\t) that
appear at the beginning of the string.
'''
# page 357


