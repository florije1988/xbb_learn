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


def cups_to_ounces(number_of_cups):
    # "header" ("(number of cups)" is the parameter list and the number of cups is the argument [pass  position] )
    number_of_ounce = number_of_cups * 8
    return number_of_ounce


intro()

# 102