def writeFib(n):
    a= 0
    b = 1
    print(a, end = ' ')
    
    while(b < n):
        print(b, end = ' ') 
        a,b=b,a+b
      

def readFib(n):
    mylis = []
    a= 0
    b = 1
    mylis.append(a)
    
    while(b<n):
        mylis.append(b)
        a,b=b,a+b
    return mylis
