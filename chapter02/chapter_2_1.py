# -*- coding: utf-8 -*-
__author__ = 'kiwi'

# This is the begining of my learning from Python :)
print('''123 Let us go!''')
# ? why we cannot use double quote marks here
print("J'aime %s" % 'Xqq')
birthday_month = 'december'  # the month of the birthday month
print('my birthday is in %s' % birthday_month)
# the underscores(_) can be the first character in a variable name
_underscore = '_'
print('''this is underscore, %s''' % _underscore)
legalBabyName = 'Meow '  # cambelCase for variable name
print ('Cat', 1)
dollars = 6
print '1 RMB exnchanges to Canadian dollars is ', dollars, 'before'
dollars = 4.99  # no currency symbol in the value
print 'but now is', dollars, '- _ -|||'
# page 47
print type(dollars)
print type(1)

'''
check point
2.10. the variable is the piece of data with a name to store the memory
2.11
    legal
    illegal
    legal
    legal
    illegal
    legal
2.12 diff. because S is upper case and s is lower case which is recognize as different element of string here
2.13 invalid. The first letter of name fo variable cannot be integer
2.14 the value is val
2.15
    int
    float
    float
    int
    str
2.16 0
'''
opening = int(input('Bonjour! Please enter number here: '))  # input(promp) a string displays on the screen
# 小笨蛋，告诉过你了啦，这个的说是说你是传入什么值就要写成标准的格式啦比如说字符串要写成("小笨笨")

print 'The variable is: ', opening

dollars_int = int(dollars)  # dollars has already asisgned above
print dollars_int
dollars_float = float(dollars_int)
print dollars_float
# get the user's credit card number, name and expire date
card_number = int(input('Please enter your card number here: '))

name = raw_input('Please enter your full name here: ')
expireDate = input('please enter the expire month and year here: [for example: 1215 or 123]')
# Display the data
print('Here is the data you entered: '), 'card_number', card_number, \
    'name', name, ('expireDate %s' % expireDate)
print 'integer division', 8 // 2
print 'division', 7 / 5  # ? no different here  课本上是针对python3 的，这里是python 2
min_rate = 2.33
hour_input = 2.345
min_input = 23
total_rate = hour_input * 60 + min_input
print 'total_rate', total_rate

# this is the program to find the new price after discount with 20% off
originalPriceList = [20, 5, 1700, 45, 3]
discount = 0.20  # the discount is 20%
for dis in originalPriceList:
    discount_price = dis - dis * discount  # calculate the new price
    dis = discount_price  # store the new price into the item
    print 'The new price for each is: ', dis
math_division = -5 // 2
print math_division  # When the result is negative, it is rounded away from zero to the nearest integer
number_1 = 4 ** 3
number_2 = 900 % 34
number_3 = 46
avg = (number_1 + number_2 + number_3) / 3
print 'The average of three number is', avg

# here is the converter for second to hour
second = 11730
hour = second // 3600
minute = second % 3600 // 60
second = second % 3600 % 60
print 'The second convert to hour and minutes is below'
print ('The time is %d hours, %d minutes, %d seconds' % (hour, minute, second))
print int(-2.9)  # -2 because it just cut the decimal
''' checkpoint page 65
2.19
    21
    2
    31
    24
    2
    69
2.20 the result is: 4
2.21   the result is: 1
'''
# ？? print 'XDD', end ==' ' end is the unresolve reference here？？ why
# 不知道你要干嘛……你不知道怎么定义么？？？先定义在使用！！！
print ('XFF\nILY')
# 你到底在干嘛！！！在这么随意写代码，就打你了！
print('Hello!\there is yours\tdo you want to have a look\n i believe you \\want to say \"no\" isn\'t it?')
print 'XDD is ' + \
      'really smart!'
number = format(123.2384767865, '.2f')  # keep two decimal
print number
amount_due = 3456.23
monthly_payment = amount_due / 12
print('This monthly payment is', format(amount_due, '.2f'))
print('e is used for: ', format(234465254.349, '.2e'))  # scientific notation, keep 2 decimal
print ('E is used for: ', format(234465254.349, ' E'))  # E is the same as e indicating the exponent
print('insert a comma here for thousand point: ', format(234465254.349, ',.3f'))
print ('leave the space before the number at about 10 space, you can use it without a comma, too, just incase :O ')
print (1, format(5254.349, '7,.3f'), 3)
# ? no space leave here???
print('the space control would be made by python automatically to make the dot at the same location')
print('we can display \'%\' as the symbol now! ', format(0.65, '.0%'))
print('here is the integer: ', format(1236787643, 'd'))
'''
review page 73
c c b b a / c a b d a / b d b a a / c a b a b
True or False
T T F T F
short answer
1. answered
2. the natural language was written as the program language
3.
4. the float would be the result
5. the floating point division is the / which would be type float in the result and keep it as the float
the integer is the number which displayed the result as the integer without any decimal
'''
# Algothm Workbench  page 76
#1
height = raw_input('Please enter your height by number here: (unit is meter)')
print height
#2
colour = raw_input('Please enter your favourite colour here: ')
print colour
#3
a = raw_input('please enter the number here: ')
a = ((4 * (a + 2)) / 3.14) - 8
#4
w = 5
x = 4
y = 8
z = 2
print 'x', x, 'y', y, 'z', z, 'w', w
print 'x + y is ', x + y
print 'z * 2 is ', z * 2
print 'y/x is', y/x
print 'y-z is', y-z
print 'w//z is ', w//z
#5
total = 10 + 14
print total
#6
down_payment = 0
due = total - down_payment
#7
subtotal = total / 0.15
print total
# 8
a = 5
b = 12
c = 30
result = a + b + c
print 'The result is: ', result
#9 the following disaplys is 5
#10
sale = format(24.34724, '.2f')
print sale
#11
number = 13234876.238467
print 'The number in question 11 is ',format(number, ',.1f')
#12 George@John@Paul@Ringo

# 你暂时不用管理input，这个在python 3里面已经统一了，还有字符串的部分。在python 2 里面是区分input以及raw_input的。
# Programming Exercises
# 1 personal information
