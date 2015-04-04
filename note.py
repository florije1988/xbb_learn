__author__ = 'kiwi'


# sorting

def bubble_sort(a_list):
    swap = True
    end = len(a_list) - 1
    while swap:
        swap = False
        for i in range(0, end):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                swap = True
                end -= 1


def another_one(a_list):
    # The complexity is O(mn), if one of then is i = i/2, the choose the other one as the complexity
    n = len(a_list)
    m = n * 4
    for i in range(0, n):
        for j in range(0, m):
            print i, j


def mystery(a_list):
    for i in range(len(a_list) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, i + 1):
            if a_list[location] > a_list[position_of_max]:
                a_list[position_of_max] = a_list[location]


# complexity
def example(my_list):
    n = len(my_list)
    for i in range(n):  # the complexity is O(n), the n ins constant times
        x = 2 * i % n
        for i in range(0, n):  # if it is for i in range 1000: the running times is O(1) times
            for k in range(0, n):
                x = 2 * n  # up here is O( n^2)


def split(my_list):
    # every line runs the constant time here
    # if i = 20, then it runs 6 times by half O(log n)

    i = len(my_list)
    total = 0
    while i > 0:
        total += my_list[i]
        i = i / 2
    return total

# the complexity only choose the maximum one when it is in two if
# bubble sort O(n)
# insertion sort, find the small in the list and exchange the elements O(n^2)


# step 1 start the program, main program function
if __name__ == '__main__':
    # run the function here
    my_list = [2, 3, 3, 4, 6, 3, 4, 6, 1]
    example(my_list=my_list)

'''
complexity:
complexity of a loop = (# of loop runs) * (complexity of the inside)
if statement (O(n))--> highest complexity of if, elif, else (inside if for loop)
LOOP O(n)
consecutive code --> O(X) O(Y)  MAX (O(X),O(Y)  )

sorting:
bubble, beach, selective, binary sort, insert

'''


def loop():
    my_list = [2, 3, 3, 4, 6, 3, 4, 6, 1]
    n = len(my_list)
    for i in my_list:
        for k in my_list:
            for j in my_list:
                print i, j, k
    while True:
        n = n / 2  # log x
    return i, j, k  # complexity is n^3


# node : linked list

def create_node(value):
    node = {}
    node['data'] = value  # my list 10 --> None (node dictionary )
    node['next'] = None
    return node  # {'data': value, 'next': None}


def add_node_at_data(linked_list, value):
    node = linked_list
    head_node = {}
    head_node['data'] = value
    head_node['next'] = node
    return head_node


def print_node(linked_list):
    print_list = linked_list
    while linked_list['next'] is not None:
        print linked_list['data']
        linked_list = linked_list['next']
    print linked_list['data']
    return print_list


def insert_node(linked_list, value, new_value):
    node_before = search_node(linked_list, value)  # find the node one before the location you want to insert
    if node_before is not None:  # avoid that the value can be searched in the search list

        node_after = node_before['next']
        new_node = create_node(value=new_value)  # create the node that the value you want to insert
        new_node['next'] = node_after
        node_before['next'] = new_node
        node_list = node_before

        while linked_list is not None and linked_list['data'] != value:
            linked_list = linked_list['next']
        if linked_list is not None:
            linked_list['next'] = new_node
        return linked_list


def change_node(linked_list):
    change_list = linked_list
    while change_list is not None:
        if change_list['data'] % 2 == 0:  # even number
            change_list['data'] += 1
        change_list = change_list['next']
    return linked_list


def search_node(linked_list, value):
    search_list = linked_list
    while linked_list is not None and linked_list['data'] != value:
        linked_list = linked_list['next']
    return search_list


# delete the node in the middle or at the head by specific value ()
def delete_node(linked_list, value):
    delete_list = linked_list
    if search_node(linked_list=linked_list, value=value) and delete_list is not None:  # if value can be found

        while delete_list['next']['data'] != value and delete_list['next'] is not None:
            # empty list or value not found
            delete_list = delete_list['next']
        ptr = delete_list
        node_to_delete = delete_list['next']
        delete_list['next'] = node_to_delete['next']
        # delete from middle of list
        # delete the 1st mode(The head)

    return linked_list


def list_length(linked_list):
    length_list = linked_list
    count = 0
    while length_list is not None:
        count += 1
        length_list = length_list['next']
    return count


def main():
    my_list = create_node(int(raw_input('input value for node: ')))
    my_list = add_node_at_data(my_list, value=10)
    my_list = add_node_at_data(my_list, value=20)
    my_list = add_node_at_data(my_list, value=30)
    print_node(my_list)
    node_1 = search_node(my_list, value=10)
    if node_1 is not None:  # avoid the return of node_1 is Node when the value cannot be found
        print 'node contains: ', node_1['data']
    else:
        print 'node doesn\'t found'
    change_node(linked_list=my_list)

    print insert_node(linked_list=my_list, value=10, new_value=1000)


'''
if __name__ == '__main__':
    main()
'''
# recursion:the function return(call) to itself (ex. christmas box unwrapping):
# 2 parts:base case--> termination; Recursive Case --> call same function with identical smaller problem
# (depend on the problem size within function),the condition to make it stops
def roll_dice():
    import random

    dice1 = random.randint(0, 6)
    dice2 = random.randint(0, 6)
    print dice1 + dice2
    if dice1 + dice2 == 7:
        return roll_dice()


# binary search divide the list into the medium(maybe not just one ) , less than medium and larger than medium
# use the first number to sort again
# quick sort is the sort that depend on the middle number to separate the item to the left that is the less number
# and to the right that is the larger number number there is no number need to be sort

'''
def quick(a_list):  # complexity is n*log(n) for best case, and n^2 for worse case
    run = 0
    for i in a_list:
        run += 1
        if run == 1:
            medium = [i]
            min_list = []
            min_list = []
        elif i > medium:
            min_list = min_list.append(i)
        elif i == medium:
            medium = medium.append(i)
        else:
            min_list = min_list.append(i)
    return
'''

'''
sort the first half: 3 and 2 (break down to sort until there is one element remain)
if there is one element, then make it as the list such as [40]
'''


def merge(list1, list2):
    result = []
    i, j = 0, 0  # the location is different for the list after soring and select on out from the origin list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:  # append the larger one into the newlist
            result.append(list2[i])
            i += 1
        else:
            result.append(list1[j])
            j += 1
    result += list1[i:]  # add the rest of the left when some left after right is ru out by sorting into the result
    result += list2[j:]  # same as above but right
    return result


'''
    list1 = [6,12,14]
    list2 = [4,9]
    this two list has been sort, and then begin with the first one, if the one within this two list is smaller,
    append it into the new list, sort from one item to the whole length of the list
'''


def merge_sort(alist):
    if len(alist) < 2:
        return alist
    else:
        mid = len(alist) / 2
        left = merge_sort([alist[:mid]])
        right = merge_sort([alist[mid:]])
        return merge(left, right)

# complexity is O(n*log(n)) for worst case and O(n) for the best case

'''
binary search(aList,value):
binary tree, split the list into the left,data, right

'''


def add(tree, value):
    if tree is None:
        return {'data': value, 'left': None, 'right': None}
    elif value < tree['data']:
        tree['left'] = add(tree['left'], value)
        return tree
    elif value > tree['data']:
        tree['right'] = add(tree['right'], value)
        return tree
    return tree


def search(tree, search_value):
    if tree == None:
        return False
    elif tree['data'] == search_value:
        return True
    elif search_value < tree['data']:
        return search(tree['left'], search_value)
    else:
        return search(tree['right'], search_value)


def find_maximum(tree):
    if tree['right'] is None:
        return tree['data']
    return find_maximum(tree['right'])


def height(tree):
    if tree is None:
        return 0
    hl = height(tree['left'])  # hl is the left subtree
    hr = height(tree['right'])
    return 1 + max([hl, hr])


def display(tree):
    if tree is None:
        print ''
    display(tree['left'])
    print tree['data']
    tree = None
    display(tree['right'])
    print tree


tree = None
list = [20, 2, 25, 14, 75, 90]
for d in list:
    tree = add(tree, d)

print find_maximum(tree)
print height(tree)

'''
Binary search tree
1) [40,20,17,54,72,1,9]*
				40
			20		54
		17				72
	1
		9
unblanced tree, because the length isn't the same
*: have to arrange by order(from 0 to end ), if less, go to left else right

2) [60,54,20,59,24,80]
--> is the balanced tree, there are tree of height in the tree
the complexity is O(log(n))

3) [10,20,40,60,80]
--> is a straight line to the right and the left is None
the complexity is O(n)

**: assume that they are not the same number in the binary tree
'''

# count the selected information from the BST and each 'data' is the linked list
def countPDFs(tree):
    if tree == None:
        return 0
    elif tree['data'][0] == 'pdf':
        val = 1
    else:
        val = 0
    return val + countPDFs(tree['left']) + countPDFs(tree['right'])


countPDFs(tree)

'''
March 31

deletion of BST
3 cases for ??
1. no children
2. 1 children
3. 2 children

looking for the largest on the subtree and move it up
BST: data base index, find things rapidly

binary number:
145 - base 10
	1* 10^2  4*10^1 5*10^0

110 - base 2
1*2^2  1*2^1  0*2^0



Tree Traversals
1. preorder
Beginning from the rooted to the left subtree and then to the right subtree, from top,which is the general category to the specific category

2. in order
beginning from the left child to the right child, if None, go to the root until there is no more for raising

3. post order
like merge, go to left and right at the same time
'''
