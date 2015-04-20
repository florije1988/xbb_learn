__author__ = 'kiwi'
print 'chapter 3 '
# page 83 checkpoint
'''
3.1 the function is a set of statements execute some of utility as the  to finish the task
3.2 the phrase 'divide and conquer' is: merge.It divides as the individual task to make the own task for running
3.3 repeat calling the function for runnign
3.4 The stock of category same type of task prepare for calling for running without rewriting them again
3.5 It is easy to learn about the purpose that the function do to make it as the flow chart of the steps of function;
easy for understanding teh purpose of function running
'''
# There are two function here, write one function within another function
def print_XDD():
    print 'You are XDD'
    print print_XBB()


def print_XBB():
    print 'who is XBB here? '
    print "No one knows !!"

# print_XDD()
'''
checkpoint page 89
3.6 A function definition has two parts. They are: the head of the function and the statement.
The head function is the statement to begin the function by call the function with using the function name(parameter)
The statement is the statment at least indent after the head function
3.7 'calling a function ' means : the function was called to execute.
If the function doesn't call, the function won't execute at all.
3.8 When a function is executing, when the end of the function's block is reached, if the blank lines that appear in a
block are ignored.When the function is at the function's block, it finishes running
3.9 the reason that i indent the statement in a block is: the sign of ending the function running
'''
# 91 Hlerarchy(structure) chart: logical chart <-- top down design (only one line )
# page 97 variables' scope


def print_all():
    print_XBB()
    print_XBB()
    print_XDD()

# print_all()

'''
page 97 check point
3.10 the loval variables is the vaiables was chreate and can be used and only be accessed within the function
the local variable can be restricted by calling the function
3.11 The variable's scope is part of program that the variables can be accessed
3.12 It isn't permissible for a local variable in one function to have the same name as a local variable in a different
function
'''


def reputation_XDD(adjective):
    print 'the reputation that i have for XDD is %s' % adjective
    return adjective


# reputation_XDD('Kawaiine')

# page 100 IN the spotlight:
# the function convert cups to fluid ounces
def intro():
    # 1. Display an introductory screen that explains what the program does.
    print 'This program is going to convert the cups to fluid ounces '
    print('reference the formula is:')
    print(' 1 cup = 8 fluid ounces')
    number_of_cups = int(raw_input('Please enter the numbers of cups here for converting: '))
    print 'The number of cups that you enter is: %s ' % number_of_cups
    print 'The ounce after converting is %s ' % cups_to_ounces(number_of_cups)


def cups_to_ounces(number_of_cup):  # parameter_name is the number of the cup
    # "header" ("(number of cups)" is the parameter list and the number of cups is the argument [pass  position] )
    number_of_ounce = number_of_cup * 8
    return number_of_ounce


def calculate_product():  # 'pass by value' from parameter
    milk = cups_to_ounces(number_of_cup=4)
    print 'The volumn of milk is: ', milk, 'ounces. '
    tomato_sauce = cups_to_ounces(number_of_cup=1)
    print 'The volumn of tomato sauce is: ', tomato_sauce, 'ounces. '
    drink = cups_to_ounces(number_of_cup=10)
    print 'The volumn of drink is : ', format(drink, ',.2f'), 'ounces. '

# page 106: print('The simple interest will be $', format(interest, ',.2f'),  sep='')
# sep = '' is the syntax error , in python 3 ??

'''
page 107 checkpoint
3.13    keyword argument
3.14    parameter
3.15    the valid value for passing by
3.16    the changes of value of parameters , yes it does when it is the pass by position
3.17    a is the statements passes by position and b is the keyword arguments
'''
my_value = 10  # global name: set the global constant, which cannot be changes


def print_out():
    print 'my value is: ', my_value


def global_name():
    global my_value  # declare the number variable, when the value changes, my value below all changes
    my_value = int(raw_input('Input my value here: '))
    print 'The input my value is: ', my_value
    show_number()


def show_number():
    print 'My value is: ', my_value


# page 110
# The following is used as a global constant; the contribution rate is the employee annual gross pay
employee_annual_gross_pay = 0.05


def total_pay():
    global employee_annual_gross_pay
    print 'The employee annual pay rate is: ', employee_annual_gross_pay * 100, '%'
    employee_annual_pay = (employee_annual_gross_pay + 1) * \
                          (float(raw_input('Please input the annual pay: $ ')))
    print 'the annual pay is: ', employee_annual_pay
    bonuses_paid = float(raw_input('Please input the bonuses  paid: $ '))
    # bonuses to their retirement plans.
    print 'The bonuses paid is: $ ', bonuses_paid
    print format(bonuses_paid + employee_annual_pay, ',.2f')

# call the function
# total_pay()

'''
page 111-112 checkpoint
3.18 The scope of a global variable is: the value which insert as the global value doesn't change at all during the
program, it is the global value constant
3.19 when the value needs to be changed more than once by the function
3.20 The global constant is the global value in the whole program is constant , it is permissible to use global constant in a program

Review Questions: ( Multiple Choice)    1~5: cbdbc   6~10: abaab    11~12:db
True or False:  1~5: TTFFT    6~10: FTTTT

Short answer:
1. call the function repeatly by calling the function with the different parameter
2. name the function is the naming the name of the function to be called; the first line is the header and the others
are the statement
3. the function stops running from the code
4. Local variables are the values in the function, the statement in the function can use the values
5. only in the function
6. The global variable may be changes from the function but it is hard to find
'''

# Algorithm Workbench
# 1
def times_ten(number):
    return number * 10


# print 'The number times ten is: ', times_ten(4)

# 2
def show_value(quantity):
    print quantity


# show_value(quantity=12)
'''
3.  a=3,b=2,c=1
4. (1,3.4)  (0,0)
5. a. 2; b. a=2; b=4; c=6
'''
# Program Exercises
# 1. kilometer converter


def kiloeter_converter(kilometer_number):
    return kilometer_number * 0.6214


# print kiloeter_converter(kilometer_number=10000), 'miles'

# 2 sale tax program refactoring
def sale_tax():
    sale = int(raw_input('Please input the sale price: '))
    print 'sale: ', sale
    tax_rate = 0.13  # 13%
    print 'tax rate: ', tax_rate
    total_sale = sale * (1 + tax_rate)
    print 'total sale: ', total_sale


#sale_tax()

# 3 how much insurance?
def min_insurance():
    property_cost = float(raw_input('Please enter the number of property cost: '))
    print 'The property cost inputed is: ', property_cost
    amount_for_buy_insurance = float(property_cost / 0.8)
    print 'Amount for insurance: ', amount_for_buy_insurance


#min_insurance()

# 4 Automobile Costs
def monthly_cost():
    print 'Please enter the price of loan payment, insurance, gas, oil, tires, and maintenance.'
    loan = enter_the_number()
    insurance = enter_the_number()
    gas = enter_the_number()
    oil = enter_the_number()
    tires = enter_the_number()
    maintenance = enter_the_number()
    return loan + insurance + gas + oil + tires + maintenance


def enter_the_number():
    return raw_input('Please enter the number here: ')


# monthly_cost()

# 5 Property tax
def property_tax():
    print 'Please input the property value below'
    property_value = enter_the_number()
    actual_value = float(property_value) * (60 / 100.00)
    print 'actual value is: ', actual_value
    tax = 0.64 / 100.00 * actual_value
    print 'The tax is: ', tax


# property_tax()

# 6. Body Mass Index
def BMI(weight, height):
    return weight * 703 / (height ** 2)

#weight = float(raw_input("Please enter the weight here: "))
#height = float(raw_input("Please enter the height here: "))
# print BMI(weight=weight, height=height)

# 7. Calories from Fat and Carbohydrates
def evaluating_diets():
    fat_grams = float(raw_input("Please enter the fat grams here: "))
    carb_grams = float(raw_input("Please enter the carb grams here: "))
    cal_fat = fat_grams * 9
    cal_carbs = carb_grams * 4
    print 'calories from fat', cal_fat
    print 'calories from carbs', cal_carbs


# evaluating_diets()
# 8. Stadium Seating
def seat_cost(num_A, num_B, num_C):
    A = 15  # For a softball game, Class A seats cost $15, Class B seats cost $12, and Class C seats cost $9.
    B = 12
    C = 9
    return num_A * A + num_B * B + num_C * C


# print seat_cost(10, 20, 30)

# 9. Paint Job Estimator
def paint_estimator():
    square = float(raw_input('Please enter the square feet of wall space to be painted '))
    price = float(raw_input('The price of the paint per gallon '))
    print 'The number of gallons of paint required', square *1.00 / 115
    print 'The hours of labor required', square * 8.00 / 115
    print 'The cost of the paint', price * square *1.00 / 115
    print 'The labor charges', square * 8.00 * 12 / 115
    print 'The total cost of the paint job', (square * 8.00 * 12 / 115) + (price * square *1.00 / 115)
#paint_estimator()
# 10. Monthly Sales Tax
def monthly_sales_tax(sale):
    state_sale_tax_rate = 0.04
    country_sale_tax_rate = 0.02
    print 'The amount of county sales tax', sale * 0.04
    print 'The amount of state sales tax', sale * 0.02
    print 'The total sales tax (county plus state)', sale * (0.04+0.02)
#monthly_sales_tax(sale=1000)


























