__author__ = 'kiwi'


def bublesort(alist):
    swap = True
    end = len(alist) - 1
    while swap:
        swap = False
        for i in range(0, end):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                swap = True
                end -= 1


def aotherone(alist):
    # The complexity is O(mn), if one of then is i = i/2, the choose the other one as the complexity
    n = len(alist)
    m = n * 4
    for i in range(0, n):
        for j in range(0, m):
            print i, j


def mystery(alist):
    for i in range(len(alist) - 1, 0, -1):
        positionofmax = 0
        for location in range(1, i + 1):
            if alist[location] > alist[positionofmax]:
                alist[positionofmax] = alist[location]


# complexity
def example(mylist):
    n = len(mylist)
    for i in range(n):  # the complexity is O(n), the n ins constant times
        x = 2 * i % n
        for i in range(0, n):  # if it is for i in range 1000: the running times is O(1) times
            for k in range(0, n):
                x = 2 * n  # up here is O( n^2)


def split(mylist):
    # every line runs the constant time here
    # if i = 20, then it runs 6 times by half O(log n)

    i = len(mylist)
    total = 0
    while i > 0:
        total += mylist[i]
        i = i / 2
    return total

# the complexity only choose the maximum one when it is in two if
# bubble sort O(n)
# insertion sort, find the small in the list and exchange the elements O(n^2)


# step 1 start the program, main program function
if __name__ == '__main__':
    # run the function here
    mylist = [2, 3, 3, 4, 6, 3, 4, 6, 1]
    example(mylist=mylist)

'''
comlexity:
complexity of a loop = (# of loop runs) * (complexity of the inside)
if statement (O(n))--> highest complexity of if, elif, else (inside if for loop)
LOOP O(n)
consecutive code --> O(X) O(Y)  MAX (O(X),O(Y)  )

sorting: 4
bubble, beach, selective, binary sort

'''


def loop():
    mylist = [2, 3, 3, 4, 6, 3, 4, 6, 1]
    n = len(mylist)
    for i in mylist:
        for k in mylist:
            for j in mylist:
                print i, j, k
    while True:
        n = n / 2  # log x
    return i, j, k


loop()
# ???? if complexity is n^3 or n^2 here