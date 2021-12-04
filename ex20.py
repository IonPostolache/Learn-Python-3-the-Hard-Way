#importing argv from sys
from sys import argv
#get arguments
script, input_file=argv

#define print_all function, which takes 1 argument (f)
def print_all(f):
    #print the contents of f
    print(f.read())
#define the rewind function, which takes 1 argument (f)
def rewind(f):
    #move the file pointer back to the begining of file f
    f.seek(0)

#define function print_a_line, which takws 2 argumnts
def print_a_line(line_count, f):
    #print line_count, then a line from file f
    print(line_count, f.readline())

#set current_file variable to a file pointer to input file
current_file=open(input_file)

#print string
print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:\n")

current_line=1
print_a_line(current_line, current_file)
"""
current_line=current_line+1
print_a_line(current_line, current_file)

current_line=current_line+1
print_a_line(current_line, current_file)
"""

current_line +=1
print_a_line(current_line, current_file)

current_line +=1
print_a_line(current_line, current_file)

#example of +=
x=3
x +=2
print(x)
