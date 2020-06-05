class SectionA :
    a = 0
    
    def setdata(self,x) :
        self.a = x

    def display(self) :
        j = 1
        for i in range(self.a,1,-1) :
            j = j*i
            print(j)

c =SectionA()
c.setdata(5)
c.display()
        
