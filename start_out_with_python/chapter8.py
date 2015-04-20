# -*- coding: utf-8 -*-
__author__ = 'kiwi'
print 'start_out_with_python 8 '
import os


def main():
    numbers = list(range(1, 10, 2))  # [1, 3, 5, 7, 9]
    another_list = numbers * 2  # repetition operator


main()

'''
page 302 checkpoint
8.1 [1, 2, 99, 4, 5]
8.2  [0,1,2]
8.3  [10,10,10,10,10]
8.4   [1,3,5,7,9]
8.5   4
8.6   use index, list.index(the_number_you_want_to_find)
8.7   [1, 2, 3]     [10, 20, 30]        [1, 2, 3, 10, 20, 30]
8.8   [1, 2, 3]     [10, 20, 30,1, 2, 3]
page 305 checkpoint
8.9 [2,3]
8.10    [2, 3, 4, 5]
8.11   [0]
8.12    [1, 2, 3, 4, 5]
8.13    [1, 2]
page 307 checkpoint
8.14    Cannot find Jasmine.    Cannot find Jasmine.    Cannot find Jasmine.    Jasmine's family: Jasmine
page 314 checkpoint
8.15 remove is for the specific item but del is depend on the location for deleting
8.16 min(alist) is for the minimum number & max(alist) is for the maximum value
8.17 both of them would use to add the string ‘Wendy’ to the list at index 0.
a is replace the item if it exits in location of 0 but
b just add another item at the end of list by remaining the original item

8.18 a. the location of the item in the list
b. put the number into the specific location without deleting other values
c. ordering the number from min to max
d. reverse the item in the list. if it is the last item, it would places into the first item
'''


# list_name[start:end:step]
# create the seperate list: list2 = []+list1 or list2 = list1[:]
def list_adding():
    item_in_list = [0, 12, 4, 56, 88]
    add_item = int(raw_input('add number: '))
    item_in_list.append(add_item)
    print item_in_list.index(12)
    item_in_list.remove(0)
    sum_item = 0
    for item in item_in_list:
        sum_item += item
        print 'item: ', item
    return 'The sum for the list is: ', sum_item


# list_adding()


def save_list():
    item_in_list = [0, 12, 4, 56, 88]
    save_file = open('new_file.txt', mode='w')
    for item in item_in_list:
        save_file.write(str(item) + '\n')
    save_file.close()


# save_list()


def read_save_in_list():
    save_file = open('new_file.txt', mode='r').readlines()
    location = 0
    for item in save_file:
        save_file[location] = item.strip('\n')
        location += 1
    print save_file
    os.remove('new_file.txt')


# read_save_in_list()

'''
page 332 checkpoint
8.19    4 * 2 --> 4 row and two column
8.20    new_list = [[0]*4]*3
8.21
numbers_list = [1, 2, 10, 20, 100, 200, 1000, 2000]
for i in raneg(0,len(numbers_list),2):
    new_list.append([number_list[i],number_list[i+1]])
page 335 checkpoint
8.22 list is mutable but tuple cannot
8.23 data cannot be changed, easy for stored,save and safe
8.24 tuple(my_list)
8.25 list(my_tuple)
page 335 Review Questions Multiple Choice
1~5  abcda  6~10 cbdcb  11~14 abdd
True or False
1~5  FTTFT   6~8 TTF
Short Answer
1. a. 5 b 0 c -1 or 4
2. 3, 1, 3
3. [4, 6]
4. [6,7]
5. [5, 6, 7, 8]
6. [2,2,2,2,2]
Algorithm Workbench
1. alist = ['Einstein', 'Newton','Copernicus','Kepler']
2. for item in list:    print item
3. number2 = number1[:]
4. insert the list, default the sum is 0,for item in list, add the item in the sum value-->return sum
5. def sum_list():
    alist = [2, 3, 4, 6, 24, 5, 5]
    alist_sum = 0
    for item in alist:
        alist_sum += item
    return alist_sum


sum_list()
6.def name_list():
    for item in name_list:
        if item == 'Ruby':
            print 'Hello Ruby'
        else:
            'No Ruby'


name_list()
7. [40, 50, 60,10, 20, 30]
8. new_list = [[]*3]*5
for row in new_list:
    for column in row:
        print new_list[row][column]
Programming Exercises
1. Total Sales
'''


def total_sales():
    total_sale = 0
    sale_list = []
    for i in range(7):
        day = float(raw_input('Input day sale: '))
        sale_list.append(day)
        total_sale += day
    return total_sale


total_sales()

# 2. Lottery Number Generator
def lottery_number():
    import random

    number = 0
    run = 0
    random_list = []
    for i in range(7):
        random_list.append(random.randint(0, 9))
    for item in random_list:
        number += 10 ** run * item
        run += 1
    return number


lottery_number()

# 3. Rainfall Statistics
def rainfall_statistics():
    rain_fall_list = [0]

    for i in range(12):
        print 'enter', i, 'month\'s rainfall below'
        rain_fall = int(raw_input('Input rainfall: '))
        rain_fall_list.append(rain_fall)
        rain_fall_list[0] = rain_fall_list[0] + rain_fall
    ave_rainfall = format(float(rain_fall_list[0]) / 12.00, ',.2f')
    rain_fall_list = rain_fall_list[1:]
    print ave_rainfall
    print min(rain_fall_list), max(rain_fall_list)


rainfall_statistics()

# 4.Number Analysis Program
def number_analysis():
    total_num = 0
    number_list = []
    for times in range(20):
        number = int(raw_input('input number: '))
        number_list.append(number)
        total_num += number
    average_num = total_num / len(number_list)
    print min(number_list)
    print max(number_list)
    print total_num
    print average_num


number_analysis()
# 5. Charge Account Validation
def charge_account():
    input_number = int(raw_input('input number: '))
    charge_account_file = open('charge_accounts.txt', 'r')
    for line in charge_account_file.readlines:
        charge_account_file.readline().strip('\n')
        if line == input_number:
            print 'valid number'
        else:
            print 'invalid number'
    print charge_account_file.realines()


charge_account()

# 6 Driver’s License Exam
def lisence_exam():
    correct_answer_list = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D', 'B', 'C', 'D', 'A', 'D', 'C', 'C',
                           'B', 'D', 'A']
    incorrect_answer_number = []
    incorrect_answer_list = []
    user_answer_list = []
    correct = 0
    for times in range(20):
        print 'number', times, ': '
        user_answer_list.append(raw_input('input answer: '))
        if user_answer_list[times] == correct_answer_list[times]:
            correct += 1
        else:
            incorrect_answer_number.append(times)
            incorrect_answer_list.append(correct_answer_list[times])
    print 'correct: ', correct
    print 'incorrect: ', 20 - correct
    print 'incorrect_answer_number', '\t', 'incorrect_answer_list'
    print incorrect_answer_number, '\t', incorrect_answer_list
    if correct >= 15:
        print 'pass the exam'
    else:
        print 'fail'


lisence_exam()
# 7. Name Search page 339
def name_search():
    girl_name = open('GirlNames.txt', 'r').readlines()
    boy_name = open('BoyNames.txt', 'r').readlines()
    input_name = raw_input('input Name: ')
    for input_name in girl_name or boy_name:
        print 'the names were among the most popular.'
    print 'the names weren\'t among the most popular.'


# name_search()

# 8. Population Data
def population_data():
    open_file = open('USPopulation.txt', 'r').realines()
    population_list = []
    increase_rate = []
    runs = 0
    for line in open_file:
        runs += 1
        population_list.append(line)
        if runs > 1:
            increase_rate.append((population_list[runs] - population_list[runs - 1]) / population_list[runs - 1])
    print 'population_list is ', population_list
    print 'The year with the greatest increase in population during the time period', max(increase_rate)
    print 'The year with the smallest increase in population during the time period', min(increase_rate)


population_data()

# 9. World Series Champions
def world_s_chamption():
    open_file = open('WorldSeriesWinners.txt','')
    year = 1903
    enter_name = raw_input('enter name: ')
    while open_file.realine != ''and year <= 2009:
        year+=1
        if enter_name == open_file.readline():
            print 'year', year
world_s_chamption()
#?? what is different between file.readlines and file.realines()
