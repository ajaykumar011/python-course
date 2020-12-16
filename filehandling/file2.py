
# Open a file
f = open("foo.txt", "wt")
f.write( "Python is a great language.\nYeah its great!!\n")

#read teh file 
f = open("foo.txt","rt")
x = f.read(10)
print("Read String is :", x)

#check the current position
position = f.tell() # get the current file position
print("The current position is: ", position)

#reposition the pointer
position = f.seek(0,0)   # bring file cursor to initial position
position = f.tell()
print("The current position is: ", position)

# a file named "geek", will be opened with the reading mode. 
f = open('foo.txt', 'r') 
# This will print every line one by one in the file 
for each in f: 
	print (each) 


# Close opend file
f.close()