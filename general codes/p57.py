try :
    open('nosuchfile')
except EnvironmentError(errno,string) :
    print("Whoops!: %s (%d)" % (string,errno))
