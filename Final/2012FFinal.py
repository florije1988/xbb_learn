# -*- coding: utf-8 -*-
__author__ = 'kiwi'
'''
Part A
1.
    a. 14
    b. 3
    c. a b c d
    d. 4 12 29
    e. [1,7,14,25]
    f. print myList[3][-1]

2.
    a. 0
    b. 0
    c. 2
    d. 4
    foo(0,2)

3.
    I love Duke
    taC
    True
    ERROR
    Duke the Wonder Cat rocks

Part B
'''


# 1
def swapPairs(list):
    for i in range(0, (len(list) / 2) + 1, 2):
        swap_item = list[i]
        list[i] = list[i + 1]
        list[i + 1] = swap_item
    return list


#print swapPairs([1, 2, 3, 4])
#print swapPairs([2, 1, 4, 6, 8])

#2
'''
start 9
start 4
x 4 2
y 4 2
x 9 4
start 7
x 7 3
start 5
x 5 2
y 5 3
y 7 5
y 9 7

'''

def recurse(n):
    if n < 4:
        return n
    else:
        print 'start',n
        x = recurse(n/2)
        print 'x',n,x
        y = recurse(n-2)
        print 'y',n,y
        return x+y
print recurse(9)
'''
# after execute
start 9
start 4
x 4 2
y 4 2
x 9 4
start 7
x 7 3
start 5
x 5 2
y 5 3
y 7 5
y 9 8
12
# where does the y  9 8 and 12 comes from

part C
1.

'''




















