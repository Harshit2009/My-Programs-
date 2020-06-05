try :
    eval("print :")
except SyntaxError,(message,(filename,lineno,offset,text)) :
    print("Error in line %d, from file %s: \n" % (lineno,filename),\
          text,"\n",\
          ' ' * offset+"^", messgae)

    
