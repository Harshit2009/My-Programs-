class a :
    rupees = 0

    def setdata(self,x) :
        self.rupees = x

class b(a) :
    def paise(self) :
        self.paise = self.rupees * 100

class c(b) :
    def display(self) :
        print("The money in paise is :"+str(self.paise))

x =c()
x.setdata(20)
x.paise()
x.display()
        
