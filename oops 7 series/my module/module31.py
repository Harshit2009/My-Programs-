class b1 :
    a =0

    def setdata(self,x) :
        self.a = x


class c1(b1) :
    def display(self) :
        for i in range(1,self.a,+1) :
            print()
            for j in range(1,i,+1) :
                print(j,end=' ')

