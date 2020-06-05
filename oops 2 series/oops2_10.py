import sys
count = 0
for argument in sys.argv :
    print("Argument %d is %s" % (count,argument))
    count += 1
