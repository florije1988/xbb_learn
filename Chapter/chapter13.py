# -*- coding: utf-8 -*-
__author__ = 'kiwi'
# chapter 13 recursion page 509

def factorial(num):
    return num * factorial(num - 1) if num - 1 >= 0 else 1

# print factorial(4)

'''
13.1 a recursive algorithm has more overhead than an iterative algorithm.
because it could not be done until the base case condition meet, the iterative algorithm depend on the range you
limited has already been set
13.2 base case is the condition to make the recursive done
13.3 The recursive case is the condition makes the code continue recursive
13.4 The base case causes a recursive algorithm to stop calling itself
13.5 The direct recursion is: directly call himself to do the recursion ; The indirect recursion is: was called by the
other function to do the recursion

page 518 Fibonacci number
Fibonacci series:
    if n = 0 , then Fib(n) =  0
    if n = 1, then Fib(n) = 1
    if n > 1, Fib(n) = Fib(n-1)+Fib(n-2)

'''


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# print fib(5)
'''
 n     fib(n - 1)      fib(n - 2)
 5      1                   1
 4      1                   0
 3      1                   0
 2      1                   0
 1      0                   None
 0      None                None
total 5

page 519 finding the greatest common divior

'''


def GCD(x, y):
    if x % y == 0:
        return y
    else:
        return GCD(y, x % y)


'''
page520
The towers of Honooi

Page 524
Multiple choice
1-5: ccada  6~10: abdba
True or False
1-4 TTFF
Short answer
1. the base case of the message is the condition that the function done with recursive and return the value back to
each seed value or the function
2. the base case is if n = 0, then factorial(n)=1; the recursive case is if n>0,factorial(n)=n*factorial(n-1)
3. The recustion ever required to solve a problem, such as fa and GCD. the searching within a file
4. because it should be end by the base case, nor the recursive would be infinite and cannot be stop
and return the result
5. reduce the size of data size or the value of number until it meet the condition in the base case

Algorithm Workbench
1. 10
2. error
'''
# 3
def traffic_sign(n):
    if n > 0:
        print 'No Parking'
        traffic_sign(n - 1)
    else:
        return None


# Programming Exercises
# 1 Recursive printing
def recursive_function(n):
    if n == 1:
        print n
        return n
    num = recursive_function(n - 1)
    print n
    return num


recursive_function(10)

# 2 recursive multiplication
def recursive_mul(x, y):
    if x > 1 and y > 1:
        return x + recursive_mul(x=x, y=y - 1)
    elif y == 1:
        return x
    else:
        return False


# print recursive_mul(7, 4)

# 3 Recursive line
def recursive_line(n):
    if n == 1:
        print '*'
        return n
    recursive = recursive_line(n - 1)
    print '*' * n
    return recursive


# recursive_line(5)

# 4 Largest list item
def find_max(list):
    if len(list) == 1:
        return list[0]
    recursive_list = find_max(list[1:])
    return recursive_list if list[0] < recursive_list else list[0]


# print find_max([2, 4, 5, 3, 6, 1, 7])

# 5 Recursive list sum
def recursive_sum(list):
    if len(list) == 1:
        return list[0]
    recursive = recursive_sum(list[1:])
    return list[0] + recursive


# print recursive_sum([2, 4, 5, 3, 6, 1, 7])

# 6 Sum of number
def sum_num(n):
    if n == 1:
        return n
    recursive = sum_num(n - 1)
    return n + recursive


#print sum_num(10)

#7 recursive power method
def power(n, exponent):
    if exponent == 1:
        return n
    recursive = power(n, exponent - 1)
    return recursive * n


#print power(2,4)

# 8 Ackermann's FUnction
def ack(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))


#print ack(3, 2)
# ?? how to recursive to get that answer






