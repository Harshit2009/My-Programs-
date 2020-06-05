class a :
    numerator = 0
    denominator = 0
    
    def setdata(self,x,y) :
        self.numerator = x
        self.denominator = y

class b(a) :        
    quotient = 0
    remainder = 0

    def quotient(self) :
        self.quotient = self.numerator / self.denominator

    def remainder(self) :
        self.remainder = self.numerator % self.denominator

class c(b) :
    def display(self) :
        print("Quotient is :"+str(self.quotient))
        print("Remainder is :"+str(self.remainder))

x =c()
x.setdata(20,10)
x.quotient()
x.remainder()
x.display()
        
