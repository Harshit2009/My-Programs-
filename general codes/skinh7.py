class b1 :
    a = 0
    b = 0
    
    def setdata(self,x,y) :
        self.a = x
        self.b = y


class c1(b1) :
    def display(self) :
        if(self.a > self.b) :
            print("a is greater")
        else :
            print("b is greater")

c = c1()
c.setdata(200,30)
c.display()
        
