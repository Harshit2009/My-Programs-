class SectionA :
    a = 0
    
    def setdata(self,x) :
        self.a = x

    def display(self) :
        j=1
        for i in range(self.a,6,+1) :
            j = j*i
            print(j)

c =SectionA()
c.setdata(1)
c.display()
        
