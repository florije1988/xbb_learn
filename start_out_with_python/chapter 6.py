# -*- coding: utf-8 -*-
__author__ = 'kiwi'
print 'chapter 6 '
import random


def random_num():
    import random

    return random.randint(1, 100)  # 1 and 100 here is the arguement


random_num()


def dice():
    string = 'y'
    print 'Rolling the dice...'
    while string == ('y' or 'Y'):
        print random.randint(1, 6)
        string = raw_input('y or Y for continuing: ')
    return False


# dice()

def repeat_value():
    Tosses = 10
    number = random.uniform(1.0, 10.0)  # return as the uniform for the floating number
    new_number = random.seed(100)  # seed value is the value would be return next time in the random operator
    print number
    print new_number
    for i in range(Tosses):
        coin = random.randint(1, 2)
        if coin == 1:
            print 'Head'
        elif coin == 2:
            print 'Tail'
        else:
            return False

# repeat_value()
# ? different between random.randint() & random.randrange() & random/uniform()
# http://blog.sina.com.cn/s/blog_470302440100ev9e.html
'''
page 213 checkpoint
6.1 the value returning can return the value back to the result of function for displaying or passing the value to
the other place after runnign the function
6.2 library function is the function has already been set up by python program which you can use by calling,
such as 'range','print'
6.3 because the script inside there do not needs to rewrite but output directly
6.4 random one time of random number by the range of 1 to 100
6.5 display the random number once in the range of 1 to 20
6.6 display the random number but only display the one in range of 10 to 20
6.7 random any number include float number nd integer
6.8 random the float number between 0.1 to 0.5
6.9 to save the value from random operator in the specific of times from initial
6.10 the random number doesn't be changed even though the random operator was used
page 225 checkpoint
6.11  for return the result from the function
6.12
a)  do_something
b)  calculate 2 times of number
c)  20
6.13 boolean function is the one by returning True or False to learn the statu
'''
import math


def cal():
    # get the number
    number = float(raw_input('Please input the number here: '))
    square_root_number = math.sqrt(number)
    print 'square root', square_root_number
    c = math.hypot(3, 4)  # triangle
    print 'c', c
    b = math.ceil(number)  # smallest integer
    print 'b', b
    d = math.floor(number)  # largest integer that is less than or equal to x, no consider about 0.4 or 0.5
    print 'd', d
    return square_root_number

# cal()
'''
page 227 checkpoint
6.14 import math
6.15 import math , square_root = math.sqrt(100)
6.16 import math radiance = math.radiance(45)
'''


def circle():
    radius = float(raw_input('Input radius: '))
    circumference = math.pi * 2 * radius
    area = math.pi * (radius) ** 2
    print 'circumference', format(circumference, ',.2f')
    print 'area', format(area, ',.2f')

#circle()

'''
page 232 Review Questions Multiple Choice
1~5 bdbad   6~10 dbccc
True or False
1~5 TFTTT
Short Answer
1. random_number = random.randrange(0,30,5) import random
2. return value
3. input, process, output
4. retest True or False
5. easy for display and seperate the structure for using
Algorithm Workbench
1. import random        random_number = random.randrange(1,100)     return random_number
2. def half(number):
    number = float(number)
  return number
3.
def cube(num):
    return num**3
def main():
    return cub(4)
4. def times_ten(number):
return number*10
5. def get_fist_name():
    return raw_input('enter his or her first name')
Programming Exercises
'''
# 1.Feet to Inches
def feet_to_inches(foot):
    feet = foot * 12
    return feet


#print feet_to_inches(float(raw_input('input foot')))
# 2.Math Quiz
def random_twice():
    sum = 0
    for _ in range(2):
        sum += (random.randint(0, 100))
    return sum


#print random_twice()
# 3.Maximum of Two Values
def maximum(value1, value2):
    if value1 > value2:
        return value1
    return value2


#print maximum(24,20)
# 4.Falling Distance
def falling_distance():
    g = 9.8
    t = float(raw_input('the amount of time in seconds, that the object has been falling: '))
    d = (1 / 2.00) * g * (t ** 2)
    return d


#print falling_distance()
# 5.Kinetic Energy
def kinetic_energy():
    m = int(raw_input('Input m: '))  # the object’s mass in kilograms
    v = int(raw_input('Input v: '))  # the object’s velocity in meters per second.
    KE = (1 / 2) * m * (v ** 2)
    return KE


#print kinetic_energy()
# 6.Test Average and Grade
def calc_average(value1, value2, value3, value4, value5):
    return (value1 + value2 + value3 + value4 + value5) / 5.00


def determine_grade():
    value1 = float(raw_input('enter the score: '))
    value2 = float(raw_input('enter the score: '))
    value3 = float(raw_input('enter the score: '))
    value4 = float(raw_input('enter the score: '))
    value5 = float(raw_input('enter the score: '))
    average = calc_average(value1=value1, value2=value2, value3=value3, value4=value4, value5=value5)
    print 'value1 is: ', value1
    print 'value2 is: ', value2
    print 'value3 is: ', value3
    print 'value4 is: ', value4
    print 'value5 is: ', value5
    print 'avergae: ', average


# 7.Odd/Even Counter
def test_odd_even():
    even = 0
    odd = 0
    for i in range(100):
        if random.randint(0, 100) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


even, odd = test_odd_even()
print 'there are %d even number' % even
print 'there are %d odd number' % odd

# 8.Prime Numbers
def is_prime(one_num):
    one_num = int(raw_input('input one number: '))
    another_num = int(raw_input('input another numer: '))
    if one_num % another_num == 0:
        return True
    return False


# 9. Prime Number List
def if_is_prime():
    random_number = random.randrange(1, 100)
    return is_prime(one_num=random_number)


if_is_prime()
# 10. Future Value
def future_value():
    P = float(raw_input('input P number: '))
    i = float(raw_input('input i number: '))
    t = float(raw_input('input t number: '))
    return P * (1 + i) ** t


print 'The furure value is: ', future_value()
# 11. Random Number Guessing Game
def guessing_game():
    import random

    input_number = int(raw_input('Input number: '))
    random_num = random.randint(1, 100)
    if input_number < random_num:
        print 'Too low, try again.'
    elif input_number > random_num:
        print 'Too high, try again.'
    else:
        return True


guessing_game()
# 12. Rock, Paper, Scissors Game
def random_RPS():
    random_num = random.randint(1, 3)
    if random_num == 1:
        flag = 'Rock'
    elif random_num == 2:
        flag = 'Paper'
    elif random_num == 3:
        flag = 'Scissprs'
    else:
        flag = 'error'
    return flag


def game():
    flag1 = raw_input('Please input “rock”, “paper”, or “scissors”: ')
    flag2 = random_RPS()
    if flag1 == flag2:
        return 'the game must be played again to determine the winner.'
    elif flag1 == 'rock':
        if flag2 == 'scissors':
            return 'user wins'
        else:
            return 'computer win'
    elif flag1 == 'paper':
        if flag2 == 'rock':
            return 'user wins'
        else:
            return 'computer win'
    elif flag1 == 'scissors':
        if flag2 == 'papper':
            return 'user wins'
        else:
            return 'computer win'
    else:
        return False


game()

















