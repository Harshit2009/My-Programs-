CustomError = 'Error'

def test() :
    raise 'Error'

try :
    test()
except CustomError :
    print("Error!")
