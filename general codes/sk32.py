class SectionA :
    a =0

    def setdata(self,x) :
        self.a = x

    def display(self) :
        for i in range(1,self.a,+1) :
            print()
            for j in range(0,i,+1) :
                print(i,end=' ')

c = SectionA()
c.setdata(5)
c.display()
