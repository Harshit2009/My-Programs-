class SectionA :
    a =0

    def setdata(self,x) :
        self.a = x

    def display(self) :
        n = 1
        for i in range(1,self.a,+1) :
            print()
            for j in range(1,i,+1) :
                print(n,end=' ')
                n = n + 1

c = SectionA()
c.setdata(6)
c.display()
