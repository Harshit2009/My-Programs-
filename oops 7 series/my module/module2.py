class a :
    rupees = 0

    def setdata(self,x) :
        self.rupees = x

class b(a) :
    def paise(self) :
        self.paise = self.rupees * 100

    def display(self) :
        print("The money in paise is :"+str(self.paise))

