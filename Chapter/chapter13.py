# -*- coding: utf-8 -*-
__author__ = 'kiwi'
# chapter 13 recursion

def factorial(num):
    return num * factorial(num-1) if num-1 >= 0 else 1

#print factorial(4)

'''
13.1 a recursive algorithm has more overhead than an iterative algorithm.
because it could not be done until the base case condition meet, the iterative algorithm depend on the range you
limited has already been set
13.2 base case is the condition to make the recursive done
13.3 The recursive case is the condition makes the code continue recursive
13.4 The base case causes a recursive algorithm to stop calling itself
13.5 The direct recursion is: directly call himself to do the recursion ; The indirect recursion is: was called by the
other function to do the recursion

'''
