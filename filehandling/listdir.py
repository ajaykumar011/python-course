import os
x = os.listdir()
print (x)

files_path = [os.path.abspath(x) for x in os.listdir()]
print(files_path)

print("Printing the directories and files in the filehandling dir")
y = os.listdir("./filehandling")
print(y)

cwd= os.getcwd()
print("Present working directory is " + cwd)