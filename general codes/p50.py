def divide(x,y) :
    return x/y

def calc(x,y) :
    return x*(divide(x,y))

try :
    print (calc(24,0))
except :
    print ("Whoa!: Those numbers don't seem to work")
