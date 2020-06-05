class a :
    p = 0
    q = 0

    def setdata(self,x,y) :
        self.p = x
        self.q = y

class b(a) :
    sum = 0
    
    def sum(self) :
        self.sum = self.p + self.q

    def display(self) :
        print(self.sum)

