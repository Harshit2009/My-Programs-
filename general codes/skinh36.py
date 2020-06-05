class a :
    aa = 0
    bb = 0

    def setdata (self,x,y) :
        self.aa = x
        self.bb = y

class b(a) :
    sum = 0
    def sum(self) :
        self.sum = self.aa + self.bb

class c(b) :
    def display(self) :        
        print(self.sum)

x = c()
x.setdata(10,10)
x.sum()
x.display()
