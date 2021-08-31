def fact(num):
    if num > 1:
        return num * fact(num - 1)
    else:
        return num

print('enter number')
a=int(input())

if(a==0):
    print('Not Possible')
else:
    print(fact(a))
    
