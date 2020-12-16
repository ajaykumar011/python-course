# File Handling
# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

import os

cwd= os.getcwd()
print("Present working directory is " + cwd)

#give the file path to locate the file.
f = open("./filehandling/demofile.txt","rt")
print(f.read())
print(f.read(5)) # reads only 5 characters

#You can return one line by using the readline() method:

f = open("secondfile.txt","r")
print(f.readline()) #shows the first line
print(f.readline()) #shows the second line

#What is Python readline()? 
# #Python readline() method will return a line from the file when called. readlines() method will return all the lines in a file in the format of a list where each element is a line in the file

print("Readlines shows each lines in the format of list")
print(f.readlines())
f.close()