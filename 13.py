def checkTriangle(a,b,c):    
    if((a * a) + (b*b) == (c * c)):
        print(True)
    else:
        print(False)
        


print('Enter 3 lengths')
a=float(input())
b=float(input())
c=float(input())

if(a>b and a>c):
    checkTriangle(b,c,a)
elif(b>a and b>c):
    checkTriangle(a,c,b)
elif(c>a and c>b):
    checkTriangle(a,b,c)
else:
    print(False)
    