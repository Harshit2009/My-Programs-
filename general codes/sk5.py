class SectionA :
    numerator = 0
    denominator = 0
    quotient = 0
    remainder = 0

    def setdata(self,x,y) :
        self.numerator = x
        self.denominator = y

    def quotient(self) :
        self.quotient = self.numerator / self.denominator

    def remainder(self) :
        self.remainder = self.numerator % self.denominator

    def display(self) :
        print("Quotient is :"+str(self.quotient))
        print("Remainder is :"+str(self.remainder))

c =SectionA()
c.setdata(20,10)
c.quotient()
c.remainder()
c.display()
        
