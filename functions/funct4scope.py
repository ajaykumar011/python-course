x = 400
def myfunc():
  #global x  #switch on and off to see the global variable effect.
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
print(x)

#output 300 400