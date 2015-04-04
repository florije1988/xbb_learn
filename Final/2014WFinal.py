# -*- coding: utf-8 -*-
__author__ = 'kiwi'

'''

CISC 121 final 2014 April( --T : Correct)

Part A:
1.
>> [7,9,"dog",3]

>> 16

>> [1,2]
>> "cat"
>> [8,9]

>> False

>> ['green',3,4,"blue",6,10]

>> 3 4

>> 1 2 3

>> True

2.
    one: 1
    two: 4
    three: 0
    four: 2
    five: ERROR

3. the x is larger than 7 and not equal to 7, yes

4. 4, 'honda',102,O(1)  --T

Part B
a. cba  --T
b. racecar  --T
c. Error (length out of index) --T
d. when the len(n) == 1
e.
'''


def recurse(n):
    if len(n) == 1:
        return n
    elif len(n) > 1:
        return n[-1] + recurse(n[0:len(n) - 1])
    else:
        return None


# recurse(raw_input('Input number: '))

'''
Part C:
1. 4 --T  ***
2.
    ptr == 13, ptr2 = 18
    ptr 13-18-17-16-None
    'head' 10-11-12-13-14-15-18-17-16-None
    ptr2 18-17-16-None

3.linked list: data type to be added and removed;
 {'head': None, 'next':None}
 '''


def look(aStack):
    copy_aStack = aStack
    max_number = 0
    while copy_aStack is not None:
        if copy_aStack['head'] > max_number:
            max_number = copy_aStack['head']
        copy_aStack = copy_aStack['next']
    return max_number


def push(aStack):
    new_node = {'head': (raw_input('input new value:')), 'next': None}
    copy_aSTack = aStack
    while copy_aSTack is not None:
        copy_aSTack = copy_aSTack['next']
    copy_aSTack['next'] = new_node
    return aStack


'''
partD:
1. O(n^2)
2.
    a. O(n)
    b. O(n) -- O(n^2)
    c. O(n) --O(1) specific number
    d. O(1)
    e. O(log(n)) - O(n*log(n))
    f. O(n^2) --O(n)



partE:
1.
    a. yes
    b. yes
    c. 119 left 117
    d. O(log(n))
    e. 9

2.
    in-order: visiting all the node in order, all teh way form the left to the root to the right,
    pre-order: from all the way to the left and from bottom to the top and the go to the right side

    a. 24-39-119-63-124-399-495-365-254-123
    b.
'''


def pre_order(tree, search_value):
    if tree['head'] is not None:
        if tree['head'] == search_value:
            return True
        pre_order(tree['left'], search_value)
        pre_order(tree['right'], search_value)
    return False


'''
Part F
1. 4
2. [14,7,12,8,100]
3. [12,24,17,20]
4. O(n^2)
5.
[0,4,5,16,24,7,51]

Part G
'''

# 1
def shift(list):
    if len(list) != 0:
        new_list = []
        for i in range(len(list)):
            new_list.insert(0, list[i])
        return new_list
    else:
        return list


# print shift([])

# 2.
def test_prime(integer):  # O(n)
    for i in range(1, integer / 2):
        return True if integer % i == 0 else None
    return None

# Bonus Question
'''
1. create a new empty list,
2. test if the linked list if it is none, if yes return none or continue to 3
2. store each node, linked_list['head']into the list by order, use insert(0,value)
3. return print new_list[len(new_list/2)]
'''














