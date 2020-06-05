class SectionA :
    a = 0
    
    def setdata(self,x) :
        self.a = x

    def display(self) :
        for i in range(self.a,6,+1) :
            print()
            for j in range(1,i,+1) :
                print(j,end=' ')

c =SectionA()
c.setdata(1)
c.display()
        
