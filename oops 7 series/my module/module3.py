class b1 :
    principal = 0
    rate = 0
    time = 0
    
    def setdata(self,x,y,z) :
        self.principal = x
        self.rate = y
        self.time = z

class c1(b1) :        
    SI = 0
    def SI(self) :
        self.SI = (self.principal * self.rate * self.time)/100

    def display(self) :
        print("The Simple Interset is :"+str(self.SI))

        
