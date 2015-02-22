# -*- coding: utf-8 -*-
__author__ = 'kiwi'
print 'chapter 6 '


def random_num():
    import random

    return random.randint(1, 100)  # 1 and 100 here is the arguement


random_num()

import random


def dice():
    string = 'y'
    print 'Rolling the dice...'
    while string == 'y' or 'Y':
        print  random.randint(1, 6)
        string = raw_input('y or Y for continuing: ')


dice()
