__author__ = 'kiwi'

# complexity
def example(mylist):
    n = len(mylist)
    for i in range(n):  # the complexity is O(n), the n ins constant times
        x = 2 * i % n
        for i in range(0,n): # if it is for i in range 1000: the running times is O(1) times
            for k in range(0,n):
                x = 2 * n # up here is O( n^2)

def split(mylist):
    # every line runs the constant time here
    # if i = 20, then it runs 6 times by half O(log n)

    i = len(mylist)
    total = 0
    while i > 0:
        total += mylist[i]
        i = i/2
    return total

# the complexity only choose the maximum one when it is in two if



# step 1 start the program, main program function
if __name__ == '__main__':
    # run the function here
    mylist = [2, 3, 3, 4, 6, 3, 4, 6, 1]
    example(mylist= mylist)
