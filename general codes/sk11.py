class SectionA :
    a = 0
    
    def setdata(self,x) :
        self.a = x

    def display(self) :
        for i in range(self.a,11,+1) :
            print(i)

c =SectionA()
c.setdata(1)
c.display()
        
