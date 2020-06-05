class b1 :
    rupees = 0

    def setdata(self,x) :
        self.rupees = x

class c1(b1) :
    def paise(self) :
        self.paise = self.rupees * 100

    def display(self) :
        print("The money in paise is :"+str(self.paise))

c =c1()
c.setdata(2)
c.paise()
c.display()
        
