import sys

def cmpval(tuple1, tuple2) :
    return cmp(tuple2[1], tuple1[1])

hostaccess = {}
urlaccess = {}

try :
    file = open("file1.py")
except :
    print("Whoa! , Couldn't open the file", +str(file1.py))
    sys.exit(1)

while 1 :
    line = file.readline()
    if line :
        splitline = line.split(line)
        if len(splitline) < 10 :
            print (splitline)
            continue

        try :
            hostaccess[host] = hostaccess[host] + 1
        except :
            hostaccess[host] = 1
        try :
            urlaccess[loc] = uraccess[loc] + 1
        except :
            urlaccess[loc] = 1
    else :
        break

hosts = hostsaccess.items()
host.sort(lambda f, s: cmp(s[1], f[1]))

for host, count in hosts:
    print (host, ":", count)

urls = urlaccess.items()
urls.sort(cmpval)

for url, count in urls :
    print (url, ": ", count)


            
    
    
