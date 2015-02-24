# -*- coding: utf-8 -*-
__author__ = 'kiwi'
print 'chapter9'

'''
page 348 checkpoint
9.1
input_word = raw_input('input word: ')
for i in input_word:
    print i
9.2 string[0]
9.3 9 or -1
9.4 indexError
9.5 len(string)
9.6 string has no effect
'''


def log_in():
    # import login
    log_in_name = (raw_input('first_name: '))[:3]
    log_in_name += (raw_input('last_name: '))[:3]
    log_in_name += (raw_input('id number: '))[-3:]
    return log_in_name


# print log_in()
'''
page 352 checkpoint
9.7 cde
9.8 defg
9.9 abc
9.10 abcdefg
'''


def test_string():
    input_string = raw_input('input string: ')
    for i in input_string:
        if input_string.isdigit() is True:
            print 'all are digits'
        elif input_string == 'q':
            print 'incldue q '
        elif 'like' not in input_string:
            print 'no like inside the string'

# test_string()

# isalnum(), isalpha(), isdigit(), islower(), isspace(), isupper()  <-- testing
# string.lower(), lstrip(), upper(),strip() <-- changing
'''???
page 356 lstrip() Returns a copy of the string with all leading whitespace characters removed.
Leading whitespace characters are spaces, newlines (\n), and tabs (\t) that
appear at the beginning of the string.
'''


def string():
    string = 'python'
    print string
    print string.endswith('cisc')  # boolean
    print string.find('p')
    string = string.replace('on', 'onisia')
    print string
    print string.startswith('Hi!')  # boolean
    print string.endswith('ia')
    if string.endswith('iq'):
        print 'Ture endswith'

# string()

# mystring.split() # default to seperate or by string by space into the item in the list
'''
page 364 checkpoint
9.11 if 'd' in mystring:
9.12 string = 'big'  string.lower()     string.replace('big','little')
9.13 if string.isdigit:    print 'contains a numeric digit'  if not string.isdigit(): print 'no digit '
9.14    a   A
9.15    for i in 'Do you want to repeat the program or quit? (R/Q)': if i == 'R' or 'r' or 'q' or 'Q': return None
9.16    $
9.17
def is_upper():
    enter_string = raw_input('Enter String: ')
    for i in enter_string:
        run = 0
        if i.isupper():
            run += 1
    return run


is_upper()

9.18 days.split()
9.19 values.aplit('$')
page 365        Review Questions        Multiple Choice
1~5 cdbca  6~10 cdabd
True or False
1~5  FTTTT
Short Answer
1. yesnoyes
2. abcabcabc
3. cde
4. [5,6]
5. joe  JOE  joe
Algorithm Workbench
1. if choice.lower() == 'y':
2.
run = 0
for i in string:
    if i == ' ':
        run += 1
3. if i.isdigit:
        run+=1
4. if i.islower:
        run+= 1
5. if not string.endswith('.com'):
    return False
6. if i == 't':
        i.upper()
7. print string[len(string):0]
8. string[:3]
9. string[-3:]
10. mytring.split('>')
Programming Exercises
'''
# 1. Initials
def initial():
    first_name = raw_input('input first name: ')
    middle_name = raw_input('input middle name: ')
    last_name = raw_input('input last name: ')
    print first_name.upper()[:1], '.', middle_name.upper()[:1], '.', last_name.upper()[:1]


initial()
# 2. Sum of Digits in a String
def sum_digit():
    sum_single_digit = 0
    input_digit = raw_input('input number: ')
    for i in input_digit:
        sum_single_digit += int(i)
    return sum_single_digit


sum_digit()

# 3. Date Printer
def read_string():
    input_date = raw_input('input date: ')
    date_list = input_date.split('/')
    if str(date_list[0]) == str(03):
        date_list[0] = 'March'
    # ...
    print date_list[0], ' ', date_list[1], ', ', date_list[2]


read_string()
# 4. Morse Code Converter
def morse():
    input_string = raw_input('input string: ')
    for i in input_string:
        if i.upper() == 'A':
            input_string.replace(input_string[i], '. –')
        elif i == '3':
            input_string.replace(input_string[i], '. . . – –')
    return input_string


morse()

# 5. Alphabetic Telephone Number Translator
def find_letter():
    enter_string = raw_input('enter string: ')
    for i in enter_string:
        if i.upper() in ['A', 'B', 'C']:
            enter_string.replace(enter_string[i], '2')
        elif i.upper() in ['D', 'E', 'F']:
            enter_string.replace(enter_string[i], '3')
            # ...
    return enter_string


find_letter()
# 6 Average Number of Words
def ave_number_word():
    each_line = 0
    line_number = 0
    open_file = open('text.txt', 'r').realines()
    for line in open_file:
        line_number += 1
        for _ in line:
            each_line += 1
    return each_line / line_number


ave_number_word()
# 7. Character Analysis
def analysis():
    a_file = open('text.txt', 'r')
    upper = 0
    lower = 0
    digit = 0
    whitespace = 0
    for line in a_file.readlines():
        for character in line:
            if character.isupper():
                upper += 1
            elif character.islower():
                lower += 1
            elif character.isdigit():
                digit += 1
            elif character == ' ':
                whitespace += 1
            else:
                return False


analysis()
# 8. Sentence Capitalizer
def capitalise():
    input_string = raw_input('input string: ')
    input_string.split('.')
    new_string = ' '
    for item in input_string:
        item = item.replace(item[0], item[0].upper())
        new_string += (item + ' ')
    return new_string


capitalise()
# 9. Vowels and Consonants
def V_C():
    vowels = 0
    consonant = 0
    input_string = raw_input('input string: ')
    for i in input_string:
        if i.lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
        else:
            consonant += 1
    return vowels, consonant


V_C()
# 10. Most Frequent Character
def most_fre():
    input_string = raw_input('input string: ')
    dictionary = {}
    for i in input_string:
        if i.lower() in dictionary.keys():
            dictionary[str(i)] += 1
        elif i.lower() not in dictionary.keys():
            dictionary[str(i)] = 1
        else:
            return False
    for i, u in dictionary:
        i, u = u, i

    return max(list(dictionary.keys())), dictionary[str(max(list(dictionary.keys())))]


most_fre()
# 11. Word Separator
def word_separator():
    input_string = raw_input('input string: ')
    flag = 1
    new_string = ''
    for i in input_string:
        if i.isupper():
            new_string = new_string + ' ' + i
        else:
            new_string += i
    return new_string


word_separator()
# 12. Pig Latin
def pig_latin():
    input_string = raw_input('input string: ').split()
    new_string = ''
    for item in input_string:
        first_letter_ay = item[0] + 'AY'
        item = item[1:] + first_letter_ay + ' '
    return str(input_string)


pig_latin()
























