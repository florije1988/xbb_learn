# -*- coding: utf-8 -*-
__author__ = 'kiwi'
print 'chapter 4'  # page 117
# if statement: first line is clause
# boolean function: true or false '==' or  '!='
def test_score(score):
    if score > 95:
        return 'Congratulate the user'  # statement after if is the statement's block when condition fittable
    else:
        return None

# test_score(score=90)
# test_score(score=98)
'''
page 125 checkpoint
4.1 The control structure is : test statement for the lines of codes for running
4.2 The decision structure is : test if the conditions is fittable for the way for executing in the next steps
4.3 boolean structure : True in False
4.4 The true and false statement for testing
4.5 Relationship between the number for testing, equality operator, unequal operator ...  >, <, <=, >=, ==, !=
4.6 if x == 0: ; if  y == 20:
4.7 if commisionRate == 0.2 ; if sales >= 10000:
'''
OT_MULTIPLIER = float(1.5)
BASE_HOURS = 40


def calc_pay_main(hours, wage):
    global BASE_HOURS
    if hours > BASE_HOURS:
        calc_pay_with_OT(wage=wage)
    else:
        calc_regular_pay(wage=wage)


print calc_pay_main(raw_input('Please enter the hours here: '), raw_input('Please enter the numebr of wage here: '))


def calc_pay_with_OT(wage):
    global OT_MULTIPLIER
    return 'The wage after 1.5 times is: ', format(float(wage) * OT_MULTIPLIER, ',.2f')


def calc_regular_pay(wage):
    return 'The regular wage is: ', format(wage, ',.2f')


'''
page 130 checkpoint
4.8 depend on the if statement it is true
4.9 if statement and else if it is needs (boolean statement if it is true or false)
4.10 when the 'if' statement is false

page 133 checkpoint
4.11 z is not less than a.
4.12  Boston    New York
'''
# Figure 4-14 page 136
def test_customer(salary, year_on_job):
    if salary >= 30000:
        if year_on_job >= 2:
            print 'You qualify for the loan.'
        else:
            print 'You must have been employed for at least two years to qualify.'
    else:
        return None


test_customer(salary=40000, year_on_job=4)
'''
page 142 checkpoint 4.13
    if number == 1:
        print('One')
    eife number == 2:
        print('Two')
    elif number == 3:
        print('Three')
    else:
        print('Unknown')
page 148 checkpoint
4.14 Boolean expression is if-elif-else expression
4.15 FTFF TTF FT
4.16 T F T T
4.17 and is both condition should be true and or is either one of the conditions is true is true
4.18 if x > 0 and x < 200:
4.19 if x < 0 or x > 200:
checkpoint in page 150
4.20 string and integer
4.21 the flag variable is the signal when some conditions is true
Review Questions    Multiple choice
1~5: dbdba  6~10: bccab  11~15: ca
True or False
1~5 TFTTT
Short answer:
1. if the conditions is true, the program would run through the statement under the condition
2. if-else
3. both conditions is true for work
4. either one of the conditions is true for work
5. == or !=
6. flag is the signal when the condition is true and it can signal in the other code when the flag represent that value
to show the statement is true
Algorithm Workbench
1. if x >100:
    y = 20
    z = 40
2. if  a<10:
        b == 0
        c == 1
3. if a <10:
    b = 0
   else:
    b = 90
4.
if score >= A_SCORE:
    print('Your grade is A.')
else:
    if score >= B_SCORE:
        print('Your grade is B.')
    else:
        if score >= C_SCORE:
            print('Your grade is C.')
        else:
            if score >= D_SCORE:
                print('Your grade is D.')
            else:
                print('Your grade is F.')
5. if amount1 > 10 and amount2 < 100:
        print 'the greater of %s and %s.'  %  amount1, amount2
6. if x>24 and x<56:
    print 'Speed is normal'
   else:
    'Speed is abnormal'
7. if x< 9 or x>51:
    print “Invalid points.”
   else:
    print “Valid points.”
Programming Exercises
1. Roman Numerals
'''


def display_roman(number):
    if number == 1:
        print 'I'
    elif number == 2:
        print 'II'
    elif number == 3:
        print 'III'
    elif number == 4:
        print 'IV'
    elif number == 5:
        print 'V'
    elif number == 6:
        print 'VI'
    elif number == 7:
        print 'VII'
    elif number == 8:
        print 'VIII'
    elif number == 9:
        print 'IX'
    elif number == 10:
        print 'X'
    else:
        return False


# display_roman(number=int(raw_input('Please enter the number for display roman number here : ')))
# 2 Areas of Rectangles
def area_rectangles():
    length = float(raw_input('Please input length here: '))
    width = float(raw_input('Please input width here: '))
    area = length * width
    area_test = float(raw_input('Please input area wanted here: '))
    if area_test > area:
        return 'the area wanted is greater than the input length and width'
    else:
        return 'the area wanted is less than the input length and width'


#area_rectangles()
# 3. Mass and Weight
def weigt():
    mass = float(raw_input("Please enter an object’s mas"))
    if (mass * 9.8) > 1000:
        print 'it is too heavy'
    elif (mass * 9.8) < 10:
        print 'it is too light.'
#weigt()
# 4. Magic Dates
def magic_date():
    month = int(raw_input("please enter the number of month here: "))
    day = int(raw_input("please enter the day of month here: "))
    year = int(raw_input("please enter two digit year here: "))
    if month > 0 and month < 13 and day > 0 and day < 32 and year > 0 and year < 100:
        print int(month+day+year). split('/')
    else:
        return False
#magic_date()
# 5. Color Mixer
def colour_mixer():
    colour1 = raw_input('Please enter the colour1 here: ')
    colour2 = raw_input('Please enter the colour2 here: ')

    if (colour1 and colour2) in ('red', 'blue', 'yellow'):
        if colour1 == 'red':
            if colour2 == 'blue':
                print 'purple'
            elif colour2 == 'yellow':
                print 'orange'
        if colour1 == 'blue':
            if colour2 == 'yellow':
                print 'green'
    else:
        return 'error'
# colour_mixer()
# 6. Change for a Dollar Game
def dollar_game():
    # enter the number of pennies, nickels, dimes, and quarters.
    pennies = int(raw_input('Please enter the number of pennies here: '))
    nickels = int(raw_input('Please enter the number of nickels here: '))
    dimes = int(raw_input('Please enter the number of dimes here: '))
    quarters = int(raw_input('Please enter the number of quarters here: '))
    total = pennies * 0.01 + nickels * 0.05 + dimes * 0.1 + quarters *0.25
    if total == 1.00 :
        return 'congratulate the user for winning the game'
    elif total > 1.00:
        print "the amount entered was more than one dollar"
    elif total < 1.00:
        print 'the amount entered was less than one dollar'
    else:
        return False
# dollar_game()
# 7. Book Club Points
def book_club():
    num_book = int(raw_input('Please enter the number of book here:'))
    print 'customer purchases %d books and  earns %d points.' % num_book, num_book*15

# book_club()
# 8. Software Sales
def sale(quantity):
    if quantity >= 100:
        return quantity * (1-0.5)
    elif quantity >= 50:
        return quantity * (1-0.4)
    elif quantity >= 20:
        return quantity * (1-0.3)
    elif quantity >= 10:
        return quantity * (1-0.2)
    else:
        return False
# sale(quantity=raw_input('Input quantity: '))
# 9. Shipping Charges
def shipping_charge(weight):
    if weight > 10:
        return 3.80 * weight
    elif weight > 6:
        return 3.70 * weight
    elif weight > 2:
        return 2.20 * weight
    elif weight > 0:
        return 1.10 * weight
    else:
        return False
#shipping_charge(weight=raw_input('Input weight for shipping: '))
#10. Body Mass Index Program Enhancement
def test_weight(BMI):
    if BMI > 25:
        print 'the person is considered to be overweight.'
    elif BMI > 18.5:
        print 'A person’s weight is considered to be optimal weight'
    else:
        print 'the person is considered to be underweight.'
#test_weight(BMI=raw_input('Input BMI'))
#11. Time Calculator
def time_calculator(second):
    day = second/86400
    hours = (second%86400)/3600
    minutes = (second%86400%3600)/60
    second = second%86400%3600%60
#time_calculator(second=int(raw_input('Input seconds: ')))


































