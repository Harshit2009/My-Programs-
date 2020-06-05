class a :
    principal = 0
    rate = 0
    time = 0
    
    def setdata(self,x,y,z) :
        self.principal = x
        self.rate = y
        self.time = z

class b(a) :        
    SI = 0
    def SI(self) :
        self.SI = (self.principal * self.rate * self.time)/100

class c(b) :
    def display(self) :
        print("The Simple Interset is :"+str(self.SI))

x = c()
x.setdata(20,20,20)
x.SI()
x.display()
        
