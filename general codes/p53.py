def parsefile(filename) :
    file = open(filename, 'rw')
    print (file.readline())
    file.write('Hello World!')
    file.close()

try :
    parsefile('strings')
except EnvironmentError(errno,msg) :
    print("Error: %s (%d) whilst parsing the file" % (msg,errno))
    
