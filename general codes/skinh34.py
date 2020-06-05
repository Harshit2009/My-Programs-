class b1 :
    a =0

    def setdata(self,x) :
        self.a = x


class c1(b1) :
    def display(self) :
        n = 1
        for i in range(1,self.a,+1) :
            print()
            for j in range(1,i,+1) :
                print(n,end=' ')
                n = n + 1

c = c1()
c.setdata(6)
c.display()
