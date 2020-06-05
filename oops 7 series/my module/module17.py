class b1 :
    a = 0
    
    def setdata(self,x) :
        self.a = x


class c1(b1) :
    def display(self) :
        j = 0
        for i in range(self.a,11,+1) :
            j = j+i
            print(j)

