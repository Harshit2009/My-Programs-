class SectionA :
    a = 0
    
    def setdata(self,x) :
        self.a = x

    def display(self) :
        for i in range(self.a,6,+1) :
            print("Hello")

c =SectionA()
c.setdata(1)
c.display()
        
