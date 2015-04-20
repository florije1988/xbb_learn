# -*- coding: utf-8 -*-
__author__ = 'kiwi'
print 'chapter5'
'''
page 158 checkpoint
5.1 The repetition structure causes a statement or set of statement to execute repeat, commonly repeat as the loop
5.2 The condition-controlled loop: use a true/false condition to control the number of times that it repeats
5.3 A count-controlled loop is :  use the for loop by counting times to control the loops
page 167 check point
5.4 loop iteration is the loop repeating when then condition is True
5.5 while loop test its condition after it performs an iteration
5.6 None
5.7 infinite loop is the uncountable times for loop here which cannot be interrupted when the condition always be Trued
running the code as the group every time
'''


def while_loop():
    for item in [0, 1, 2, 3, 4, 5]:
        print item
    for second_item in range(0, 20, 4):
        print second_item


while_loop()


# loop that iterates for the square of the iterate
def square_number():
    print 'number\tsquare'
    for i in range(11, 0, -1):  # from 11 to 0
        print '  ', i, '\t', i ** 2  # exponent operator


square_number()


# convert the KPH
def convert_MPH():
    print 'KPH\tMPH'
    print '-' * 20
    for i in range(60, 131, 10):
        print i, '\t', format(i * 0.6214, ',.1f')


convert_MPH()

'''
page 178 checkpoint
5.8 for i in range(6):  print 'I love to program!'
5.9     0   1   2   3   4   5
5.10    2   3   4   5
5.11    0   100 200 300 400 500
5.12    10  9   8   7   6
page 182 checkpoint
5.13  An accumulator is the range limit
5.14 Yes, it should be an accumulator be initialized to any specific value or default as zero
5.15 1, 3, 6, 10, 15
5.16    15     5
5.17    a) quantity += 1    b) days_left -=5     c)price *= 10       d) price /= 2
page 185 checkpoint
5.18    sentinel: the value which is calculated was stored and continuing calculating
5.19    needs to learn the result after calculation each time
page 190 checkpoint
5.20  The filter of bad data in the program
5.21  filter the invalid code
5.22  use the while loop to filter the error or the bad data in the code
5.23  priming read is the while statement limit the condition for filtering the bad data
5.24  when the condition is valid in while
'''


def cycle():
    for i in range(1, 10, 2):
        while i / 2 == 0:  # nested loop is the loop within the loop
            print i
            i += 1


cycle()

# draw the rectangle by *
def rectangle():
    for row in range(0, 4, 2):
        print '*' * 6


rectangle()

'''
cannot be in the same line why??
for r in range(NUM_STEPS):
    for c in range(r):
        print(' ', end='')

Page 197 Review Questions Multiple Choice
1~5 bcaac   6~10 cdaba  11~12 dc
Ture or False
1~5 TTTFT  6~7  TF
Short answer
1. a condition-controlled loop is: the loop to control if the condition is True or not, if Ture->valid data
2. count-controlled loop is depend on the valid number for controlling the running times
3. infite loop: no way to exit for executing and looping
i = True
while i:
    print 'yes!'
4. it is the initial valuables for counting and displaying
5. learn the times and the item the loop running
6. value may be error or out of range
7. the filter of bad data or as the error inside the data
8. for controlling the data correctly
Algorithm Workbench
1. while product < 100:   product *=10
2.def sum():
    number1 = int(raw_input('Input number1: '))
    number2 = int(raw_input('Input number2: '))
    sum = number1 + number2
    return sum
print sum()
3. for i in range(0,1001,10):
4. number = int(raw_input('Input number: '))
    while number:
        print number8=10
5. j = 0
    for i in [1/30,2/29,3/28...30/1]:
        j += i
6. a x+=1   b. x*=2     c. x/=10    d. x-= 100
7. for row in raneg(15):
    for nested in range(10):
        print nested
8.  number = int(raw_input('Input number: '))
    while number <= 0:
        print 'error'
9. number = int(raw_input('Input number: '))
    while number > 1 and number < 100:
        print number
Programming Exercises
1. Bug Collector
'''


def bug_collector():
    total_number = 0
    for i in range(0, 8):
        number = int(raw_input('Input number: '))
        print total_number + number
    return total_number


bug_collector()
# 2. Calories Burned
def cal_burned():
    for min in range(10, 40, 10):
        min *= 3.9
    return min


cal_burned()
# 3. Budget Analysis
def budget():
    budget = int(raw_input('Input budget: '))
    expense = int(raw_input('Input expense: '))
    while budget > expense:
        return 'under budget'
    return 'over budget'


budget()
# 4. Distance Traveled
def dis_cal():
    mph = int(raw_input('What is the speed of the vehicle in mph? '))
    hours = int(raw_input('How many hours has it traveled? '))
    print 'hours/tdistance traveled'
    print '-' * 30
    for i in range(40, 130, 40):
        print mph, '\t', mph * hours


dis_cal()
# 5 Average Rainfall
def ave_rainfall():
    years = float(raw_input('Input years: '))
    total_incehes = 0
    for i in range(years):
        for i in range(0, 13, 1):
            inches = float(raw_input('the inches of rainfall for that month'))
            total_incehes += inches
            print 'inches', inches
    return total_incehes / years


ave_rainfall()
# 6 Celsius to Fahrenheit Table
def fah_convert():
    print 'F\tc'
    print '-' * 30
    for C in range(21):
        F = float(9 / 5) * C + 32
        print F, '\t', C


fah_convert()
# 7. Pennies for Pay
def pennies():
    sum = 0
    day = int(raw_input('Input day: '))
    for i in range(day):
        sum += 1
    return float(sum / 100)


pennies()
# 8 Sum of Numbers
def sum_num():
    sum_num = 0
    number = int(raw_input('Input number: '))
    while number > 0:
        sum_num += number
    return sum_num


sum_num()
# 9. Write a program that uses nested loops to draw this pattern:
def nest():
    for row in range(8):
        for num in range(7, 1, -1):
            print '*' * num  # ?? cannot print in the same line here


nest()
'''
*******
******
*****
****
***
**
*
'''

# 10 Write a program that uses nested loops to draw this pattern:
def space():
    for i in range(6):
        print '#', i * ' ', '#'


space()


































