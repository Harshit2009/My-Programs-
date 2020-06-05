class b1 :
    fahrenheit = 0
    
    def setdata(self,x) :
        self.fahrenheit = x

class c1(b1) :
    celcius = 0
    def celcius(self) :
        self.celcius = (self.fahrenheit - 32)*5/9

    def display(self) :
        print("The temperature in celcius is :"+str(self.celcius))

