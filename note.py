__author__ = 'kiwi'


# sorting

def bublesort(a_list):
    swap = True
    end = len(a_list) - 1
    while swap:
        swap = False
        for i in range(0, end):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                swap = True
                end -= 1


def aother_one(a_list):
    # The complexity is O(mn), if one of then is i = i/2, the choose the other one as the complexity
    n = len(a_list)
    m = n * 4
    for i in range(0, n):
        for j in range(0, m):
            print i, j


def mystery(a_list):
    for i in range(len(a_list) - 1, 0, -1):
        positionofmax = 0
        for location in range(1, i + 1):
            if a_list[location] > a_list[positionofmax]:
                a_list[positionofmax] = a_list[location]


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
comlexity:
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

def creat_node(value):
    node = {}
    node['data'] = value  # mylist 10 --> None (node dictionary )
    node['next'] = None
    return node  # {'data': value, 'next': None}


def add_node_at_data(linked_List, value):
    node = linked_List
    head_node = {}
    head_node['data'] = value
    head_node['next'] = node
    return head_node


def print_node(linked_list):
    print_list = linked_list
    while linked_list['next'] != None:
        print linked_list['data']
        linked_list = linked_list['next']
    print linked_list['data']
    return print_list


def insert_node(linked_list, value, newvalue):
    node_before = search_node(linked_list, value)  # find the node one before the location you want to insert
    if node_before != None:  # avoid that the value can be searched in the search list

        node_after = node_before['next']
        new_node = creat_node(value=newvalue)  # create the node that the value you want to insert
        new_node['next'] = node_after
        node_before['next'] = new_node
        node_list = node_before

        while linked_list != None and linked_list['data'] != value:
            linked_list = linked_list['next']
        if linked_list != None:
            linked_list['next'] = new_node
        return linked_list


def change_node(linked_list):
    change_list = linked_list
    while change_list != None:
        if change_list['data'] % 2 == 0:  # even number
            change_list['data'] = change_list['data'] + 1
        change_list = change_list['next']
    return linked_list


def search_node(linked_list, value):
    search_list = linked_list
    while linked_list != None and linked_list['data'] != value:
        linked_list = linked_list['next']
    return search_list


# delete the node in the middle or at the head by specific value ()
def delete_node(linked_list, value):
    delete_list = linked_list
    if search_node(linked_list=linked_list, value=value) and delete_list != None:  # if value can be found

        while delete_list['next']['data'] != value and delete_list['next'] != None:
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
    while length_list != None:
        count += 1
        length_list = length_list['next']
    return count


def main():
    my_list = creat_node(int(raw_input('input value for node: ')))
    my_list = add_node_at_data(my_list, value=10)
    my_list = add_node_at_data(my_list, value=20)
    my_list = add_node_at_data(my_list, value=30)
    print_node(my_list)
    node_1 = search_node(my_list, value=10)
    if node_1 != None:  # avoid the return of node_1 is Node when the value cannot be found
        print 'node contains: ', node_1['data']
    else:
        print 'node doesn\'t found'
    change_node(linked_list=my_list)

    print insert_node(linked_list=my_list, value=10, newvalue=1000)


if __name__ == '__main__':
    main()


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

def qucik_sort(a_list):
    run = 0
    for i in a_list:
        run += 1
        if run == 1:
            medium = [i]
            min = []
            max = []
        elif i > medium:
            min = min.append(i)
        elif i == medium:
            medium = medium.append(i)
        else:
            max = max.append(i)
    return





























