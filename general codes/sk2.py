class SectionA :
    rupees = 0
    paise = 0

    def setdata(self,x) :
        self.rupees = x

    def paise(self) :
        self.paise = self.rupees * 100

    def display(self) :
        print("The money in paise is :"+str(self.paise))

c =SectionA()
c.setdata(20)
c.paise()
c.display()
        
