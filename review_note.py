# -*- coding: utf-8 -*-
__author__ = 'kiwi'
'''
date: Feb. 26th review for first mid-term (beginning python and from sarting_out_with_python_2nd_edition)

list
tuple
string

sorting

'''

# list
def list_review():
    create_list = []
    print create_list, 'create_list'

    number_list = [2, 3, 4, 12, 323]  # item can be string, integter, float and other
    print number_list, 'number_list'
    print len(number_list), '\t', 'len(number_list)'

    number_list.append(1000)  # append is adding one item at the beginning of the list
    append_list = number_list
    print append_list, 'append_list  1000'

    index_item = number_list.index(3)  # return a integer represent the location in the list
    print index_item, '\t', 'index_item  3'

    number_list.insert(0, 400)
    insert_item = number_list  # number_list.insert(index= 0, item= 200)
    print insert_item, 'insert_item  400 at [0]'

    number_list.sort()
    sort_list = number_list
    print sort_list, 'sort_list'

    number_list.remove(3)
    remove_item = number_list  # number_list.remove(item= 12)
    print remove_item, 'remove_item 3'

    del number_list[0]
    del_item = number_list  # delete the item in the specific location
    print del_item, 'del_item at [0]'

    copy_list = number_list[:]
    equal_list = number_list

    number_list.reverse()
    reverse_list = number_list
    print reverse_list, 'reverse_list'

    print copy_list, 'copy_list after reverse list'
    print equal_list, 'equal_list after reverse list'

    get_slice_list = number_list[2:4]  # list[start:end:step]
    print get_slice_list, 'get_slice_list'

    print number_list[::-1], '\t', '::-1 means reverse too',
    print min(number_list), '\t', 'minimum item within the list'
    print max(number_list), '\t', 'maximum item within the list'


# list_review()


def tuples_review():
    create_tuple = ()
    print create_tuple, '\t', 'create_tuple'

    create_another_tuple = (1,)  # comma is the signal for creating a tuple
    print create_another_tuple, '\t', 'create_another_tuple'


# tuples_review()


def string_review():
    create_string = ''
    print create_string, '\t', 'create_string'
    print len(create_string), '\t', 'len(create_string)'  # return 0 here

    string = '             String 123        '
    print string, '\t', 'string'
    print len(string), '\t', 'len(string)'  # string cannot edit in the for i in string loop

    another_string = '        another        '
    print another_string, '\t', 'another_string'

    string = another_string + string  # the order of + effect the order of concatenation in the string
    print string, '\t', ' add another_string + string: '

    print string[-6:], '\t', 'slice string string[-6:]'  # string[start:end:step]
    print string[::-1], '\t', 'reverse string'

    print string.isalnum(), '\t', 'test if string contains numbers or digits '
    # Returns true if the string contains only alphabetic letters or digits
    print string.isalpha(), '\t', 'test if string contain alphabetic '
    # Returns true if the string contains only alphabetic letters
    print string.isdigit(), '\t', 'test if string contain digits '
    # Returns true if the string contains only numeric digits
    print string.islower(), '\t', 'test if string contain lower case '
    # Returns true if all of the alphabetic letters in the string are lowercase,
    print string.isspace(), '\t', 'test if string contain upper case '
    # Returns true if the string contains only whitespace characters
    # Whitespace characters are spaces, newlines (\n),tabs (\t)
    print string.isupper(), '\t', 'upper case the string'
    # Returns true if all of the alphabetic letters in the string are uppercase



    print string.upper(), '\t', 'upper case the string'  # upper case all the string
    print string.lower(), '\t', 'lower case the string'  # lowercase all the string
    print string.strip(), '\t', 'remove the leading and trailling space '

    print string.lstrip(
        'a'), '\t', 'remove the string of \'a\' in string.lstrip(a)'  # remove the string of char in string.lstrip(char)
    # ?????????

    string = string.lstrip()
    print string, '\t', 'remove leading space: lstrip'
    print string.rstrip(), '\t', ' remove trailling space: rstrip'

    print string.endswith('n'), '\t', 'test if the string ends with \'n\' '  # string.endswith(subtring)
    print string.startswith('a'), '\t', 'test if the string starts with \'a\' '
    print string.replace(string, another_string), '\t', 'replace the string from string to another string'
    # replace(old, new)
    print string.find('n'), '\t', 'find \'n\' in string'  # return location

    input_string = raw_input('input string here: (return as default as string) ')
    print input_string, '\t', 'input_string'


string_review()


'''
bubble sort: swap two between item

Selection sort: each pass, find the minimum number for selection sort

insertion sort: find the minimum in the list and then put it into the specific location they needs to , for example, find the minimum put it into first place in the first pass

only float times float


'''