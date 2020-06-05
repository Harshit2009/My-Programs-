class a :
    fahrenheit = 0
    
    def setdata(self,x) :
        self.fahrenheit = x

class b(a) :
    celcius = 0
    def celcius(self) :
        self.celcius = (self.fahrenheit - 32)*5/9

class c(b) :
    def display(self) :
        print("The temperature in celcius is :"+str(self.celcius))

x = c()
x.setdata(97)
x.celcius()
x.display()
        
