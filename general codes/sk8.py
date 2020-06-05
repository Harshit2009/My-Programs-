class SectionA :
    a = 0
    b = 0
    c = 0
    
    def setdata(self,x,y,z) :
        self.a = x
        self.b = y
        self.c = z

    def display(self) :
        if(self.a > self.b) :
            if(self.a > self.c) :
                print("a is greater")
            else :
                print("c is greater")
        else :
            if(self.b > self.c) :
                print("b is greater")
            else :
                print("c is greater")
                
c =SectionA()
c.setdata(20,30,40)
c.display()
        
