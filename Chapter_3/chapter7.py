# -*- coding: utf-8 -*-
__author__ = 'kiwi'
print 'chapter7'
# 'a' is append, If the file already exists, it will not be erased. If the file does not exist, it will be
# created. • When data is written to the file, it will be written at the end of the file’s current contents.
def main():
    new_file = open(r'new_file.txt','a')   # r' raw string
    new_file.write('Hello!\nHI!\n')    # write data in file  #? doesn't appear as the new line
    new_file.write('This is the first line\nThis is the second line!')
    new_file.write('This is the third line!\nThis is the forth line! ')
    new_file.close()
    new_file = open(r'new_file.txt','r')
    print 'readline: ',new_file.readline(),'\n'  # status display by new_file .read
    print 'readlines',new_file.readlines(),'\n'
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
        if flag == 0 :
            statu = False
    new_file.close()
#write_file()
def read_file():
    file_read = open('new_file.txt', mode='r')
    line = file_read.readline()
    while line != '':
        print int(line)
        line = file_read.readline()
    return None
#read_file()
# ? cannot stop, infinity loop here why??

'''
page 263 checkpoint
7.12 for line in file.readline:
7.13 the string is end
7.14
def file():
    data_file = open('data.txt','r')
    read_line = data_file.readline
    for read_line in data_file.readlines():
        print ' single line ',data_file
    while data_file != '':
        print ' single line ',data_file
        read_line = data_file.readline
file()
7.15  above
'''
# every piece of data is field
#   new_file.read().strip('\n')
import os
#os.remove('data.txt')
#rename('data.txt', 'new_data.txt')
# only the string can be stored as string

def main():
    flag = True
    tmp_file = open('create_file.txt', mode = 'w')
    data = raw_input('Input data: ')
    tmp_file.write(data+'\n')
#main()

def editing_data():
    read_file = open('create_file.txt', mode = 'r')
    os.remove('create_file.txt')
    read_file.read().strip('\n')
    # rename the file if needs: os.rename('new_data')
#editing_data()

'''
page 276 checkpoint
7.16
7.17
7.18
'''


















