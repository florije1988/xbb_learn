# -*- coding: utf-8 -*-
__author__ = 'kiwi'
import os
import random

print 'chapter7'
# 'a' is append, If the file already exists, it will not be erased. If the file does not exist, it will be
# created. • When data is written to the file, it will be written at the end of the file’s current contents.
def main():
    new_file = open(r'new_file.txt', 'a')  # r' raw string
    new_file.write('Hello!\nHI!\n')  # write data in file  #? doesn't appear as the new line
    new_file.write('This is the first line\nThis is the second line!')
    new_file.write('This is the third line!\nThis is the forth line! ')
    new_file.close()
    new_file = open(r'new_file.txt', 'r')
    print 'readline: ', new_file.readline(), '\n'  # status display by new_file .read
    print 'readlines', new_file.readlines(), '\n'
    new_file.read().strip('\n')  # delete the string of new line
    print new_file.readlines()

# main()

'''
checkpoint page 256
7.1 output file is display or get out the content or the method
7.2 read the file or get it from the other file
7.3 open the file(O), read the file(processing the file) and close the file(output file)
7.4 text and binary, text can be read from this program but binary cannot because it is the edition of txt program
7.5 txt can be edited and read but binary can only in specific program
7.6 open(filename,mode)
7.7 create a new file
7.8 read the method and edit it
7.9 exiting and storing the file
7.10 the string, mode = r , readline or readlines for reading the file
7.11 'w'. The content is written from the beginning
'''
# read the file by while loop: while != '':
# for i in readlines:
def write_file():
    new_file = open('new_file.txt', mode='w')
    statu = True
    while statu:
        second = raw_input('Input second: ')
        new_file.write(second)
        flag = int(raw_input('input 1 for continue input and input 0 for exits: '))
        if flag == 0:
            statu = False
    new_file.close()


# write_file()
def read_file():
    file_read = open('new_file.txt', mode='r')
    line = file_read.readline()
    while line != '':
        print int(line)
        line = file_read.readline()
    return None

# read_file()
# ? cannot stop, infinity loop here why??

'''
page 263 checkpoint
7.12 for line in file.readline:
7.13 the string is end
7.14
'''


def file():
    try:
        data_file = open('data.txt', 'r')
        read_line = data_file.readline
        for read_line in data_file.readlines():
            print ' single line ', data_file
        while data_file != '':
            print ' single line ', data_file
            read_line = data_file.readline
    except Exception as err:
        print err


file()
# 7.15  above
'''
# every piece of data is field
# new_file.read().strip('\n')
import os
# os.remove('data.txt')
# rename('data.txt', 'new_data.txt')
# only the string can be stored as string
'''


def main():
    flag = True
    tmp_file = open('create_file.txt', mode='w')
    data = raw_input('Input data: ')
    tmp_file.write(data + '\n')


# main()

def editing_data():
    read_file = open('create_file.txt', mode='r')
    os.remove('create_file.txt')
    read_file.read().strip('\n')
    # rename the file if needs: os.rename('new_data')

# editing_data()

'''
page 276 checkpoint
7.16    record is storing data in the file which able to read data when open it, field is a series of data in a record
7.17    open the file, copy the file and save it as temporary file
7.18    open the file, copy th file, save file as temporary deletes a record, rename the original file,
delete the original file in original name, instead of new file (tmp file)
'''


def calculation():
    try:
        number1 = int(raw_input('input num: '))
        number2 = int(raw_input('input num: '))
        result = number1 / number2
        print result
    except TypeError:
        print 'type error-->error'
    except Exception as err:  # exception means all error, or specific error name here
        print err
    except:
        print 'False'
    else:
        'Please try again!'


# ? cannot execute
# calculation()


def error_open_file():
    try:
        get_file = open('niew.txt', 'w')
        print get_file.read().strip('\n')
    except IOError:  # except by raising an specific error
        print 'IOError: File not open for reading'
        print 'ERROR!'
    finally:
        print 'this is finally'

# error_open_file()
'''
page 289 checkpoint
7.16 raise the exception for the error for continueing executing
7.17 the program would stop runnning by showing the error keyword
7.18 IOError
7.19 ValueError
Review Questions Multiple Choice
1~5 cbdca   6~10  bacdd    11~15 bdbab
True or False
1~5  FTFTF   6~9  FTFF
Short Answer
1. open the file, edit the file, close file
2. the data that you edited could be stored
3. from initial by ordered
4. continue from the last content for editing
5. create the field inside there as same as create the file content
Algorithm Workbench
1~2:
'''


def file_using():
    try:
        file_input = open('my_name.txt', 'w')
        name_input = raw_input('Input name: ')
        print 'name', '\t', name_input
        file_input.write(name_input + '\n')
        file_input.close()
        print 'read line: ', open('my_name.txt', mode='r').readline()
        print 'remove file: ', os.remove('my_name.txt')
    except Exception as err:
        print err


# file_using()
#3.
def create_number_line():
    try:
        number_list = open('number_list.txt', 'w')
        sum = 0
        for number in range(0, 10):
            sum += number + 1
            number_list.write(str(number + 1) + '\n')
            print 'number: ', number + 1
        number_list.write(str(sum) + '\n')  # ^^
        number_list.close()

    except Exception as err:
        print err


#4.

def read_line():
    create_number_line()
    number_list = open('number_list.txt', 'r')
    for line in number_list:
        print line.strip('\n')
    print os.remove('number_list.txt')


read_line()
'''
5.  ^^
6. number_list = open('number_list.txt','a')
7~8:
'''


def record():
    record_list = open('students.txt.', 'a')
    flag = 1
    while flag == 1:
        name = raw_input('enter name: ')
        score = raw_input('input score: ')
        record_list.write(name + '\n' + score + '\n')
        print 'name:', name
        print 'score', score
        flag = int(raw_input('intput 1 for continue, else measn exits: '))
    record_list.close()


def read_record():
    try:
        record()
        read_record_list = open('students.txt.', 'r')
        write_record_list = open('new_students.txt.', 'w')
        flag = 0
        for line in read_record_list.readlines():
            if line.strip('\n') == 'John Perz':
                print 'line includes JP: ', line.strip('\n')
                flag = 1
            elif flag == 1:
                print 'line not includes in file: ', line
                flag = 0
            elif line.strip('\n') == 'Julie Milan':
                flag = 3
            elif flag == 3:
                write_record_list.write('100')  # 8
                flag = 0
            else:
                write_record_list.write(line)
                print 'normal line is:', line.strip('\n')
        print 'new_students file: ', os.remove('new_students.txt.')
        print 'students file is ', os.remove('students.txt.')
    except Exception as err:
        print err


read_record()
'''
9.This code caused a ValueError.
10.An error happened.   The end.

Programming Exercises
1. File Display
'''


def read_int():
    try:
        read_integer = open('numbers.txt', 'r')
        while read_integer.readline() != '':
            print read_integer.readline()
        read_integer.close()
    except Exception as err:
        print err


read_int()
'''
2. File Head Display
'''


def read_int():
    try:
        run = 0
        read_integer = open('numbers.txt', 'r')
        for line in read_integer.readlines():
            run += 1
        if run > 5:
            flag = 1
        else:
            flag = 0
        if flag == 0:
            for line in read_integer.readlines():
                print line
        else:
            print read_integer.readlines()
    except Exception as err:
        print err


read_int()
'''
3. Line Numbers
4. Item Counter
5. Sum of Numbers
6. Average of Numbers
'''


def create_file():
    try:
        name = raw_input('Enter file name: ')
        new_file = open(name + '.txt', mode='w')
        run = 0
        flag = 1
        sum_num = 0
        while flag == 1:
            run += 1
            sum_num += run
            new_file.write(run)
            print 'line number is:%d' % run
        new_file.write(sum_num)  # 5
        new_file.write(str(sum_num * 1.00 / run))  #6
        new_file.close()
    except IOError:  # 9
        open(name + '.txt', 'r')
    except ValueError:
        Ave_num = int(sum_num * 1.00 / run)
        os.remove(name + '.txt')


create_file()
'''
7. Random Number File Writer
8. Random Number File Reader
'''


def random_num_file():
    total_num = 0
    random_number_file = open('random_number_list.txt', 'w')
    for i in range(100):
        random_num = random.randint(1, 100)
        total_num += random_num
        random_number_file.write(str(random_num) + '\n')
    random_number_file.close()
    random_number_file.write(str(total_num) + '\n')
    random_number_file = open('random_number_list.txt', 'r')  # 8
    for line in random_number_file.realines():
        print line.strip('\n')  # last line is the total number


random_num_file()
'''
9. Exception Handing --> 6
10. Golf Scores
1)

2)


'''


def enter_record():
    try:
        node = 1
        while node == 1:
            name = raw_input('Enter file name: ')
            score = raw_input('Enter file score: ')
            record_file = open('golf.txt', 'w')
            record_file.write(name + '\n' + score + '\n')
            print 'name: %s, score: %s' % name, score
            node = raw_input('enter 1 for contitnue or 0: ')
    except Exception as err:
        print err


def read_record():
    enter_record()
    read_file = open('golf.txt', 'r')
    for line in read_file.readlines():
        print line.strip('\n')
    print os.remove('golf.txt')


read_record()











