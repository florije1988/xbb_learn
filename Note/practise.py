# -*- coding: utf-8 -*-
__author__ = 'kiwi'


# recursion
# 1  a recursive function to sum the integers from 1 to n
def sum(value):  # value is integer here
    if value > 0:
        return value + sum(value - 1)
    return False


# print sum(raw_input('Please enter the integer here to calculate the sum from 1 to the number you enter: '))


# 2
def sum_square(m, n):
    if m <= n:
        return m ** 2 + n ** 2 + sum_square(m + 1, n - 1)  # sum of the squares of m and n
    return False
# print sum_square(int(raw_input('Enter the value m: ')),int(raw_input('Enter the value n: ')))


#3
def reverse_string(string):
    if len(string) > 0:
        reverse_string(string[1:])
        print string[0],
    return string

# reverse_string('XDD')


