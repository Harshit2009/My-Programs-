def divide(x,y) :
    returnx/y

def calc(x,y) :
    return x*(divide(x,y))

try :
    print(calc('Hello',1))
except ZeroDivisionError :
    print( "Whoa!: Your trying to divide by zero and you can't!")
except TypeError :
    print ("Whoa!: That doesn't look like a number!")
except :
    print ("Whoa!: Some other kind of error occoured!")
    
