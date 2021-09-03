def intFL(a):
    aLen = len(a)
    temp = a[0]
    a[0] = a[aLen-1]
    a[aLen-1] = temp
    return a

a = ["aa",4,-5,7,-3,2,5,534,6,-56,65,64,-6,6,-64,4,4,-6,7,-8,8,3,2,13,-31,-67,2,0]
print(a)
a = intFL(a)
print(a)
    