

a= 999

val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
syb= ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

outputVal = ''

while a> 0:
    for i in val:
        if a >= i:
            outputVal = outputVal + syb[val.index(i)]
            a = a-i
            break

print(outputVal)