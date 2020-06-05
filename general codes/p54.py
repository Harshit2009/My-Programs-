class MyNameException:
    def __init__(self,name,msg) :
        self.args = (name,msg)

try :
    raise MyNameException('Marvin','Not my real name')
except MyNameException(name,msg) :
    print('Sorry,but',name,'is',msg)
