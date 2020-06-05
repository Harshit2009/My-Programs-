class b1 :
    a =0

    def setdata(self,x) :
        self.a = x


class c1(b1) :
    def display(self) :
        for i in range(1,self.a,+1) :
            print()
            for j in range(0,i,+1) :
                print(i,end=' ')

c = c1()
c.setdata(5)
c.display()
