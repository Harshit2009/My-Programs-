class SectionA :
    a = 0
    
    def setdata(self,x) :
        self.a = x

    def display(self) :
        for i in range(self.a,0,-2) :
            print(i)

c =SectionA()
c.setdata(20)
c.display()
        
