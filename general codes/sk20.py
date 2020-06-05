class SectionA :
    a = 0
    
    def setdata(self,x) :
        self.a = x

    def display(self) :
        a = 3
        for i in range(self.a,11,+1) :
            j = a*i
            print(j)

c =SectionA()
c.setdata(1)
c.display()
        
