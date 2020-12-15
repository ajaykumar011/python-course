class Numcalc:
    def __init__(self, num):
        self.num=num
    def doublenum(self):
        return (self.num)*2

#Object defination

x=int(input("Enter your number: "))
p1=Numcalc(x)
y=p1.doublenum()
print("Result is : " + str(y))


