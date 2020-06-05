try :
    file = open('file')
except EnvironmentError :
    print("Whoops: Can't seem to open the file")
else :
    lines = file.readline()
    file.close()
