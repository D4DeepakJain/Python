# cel to farenhite

temperature = float(input())
print('1 to conver into cel, 2 for farenhite')
operation = int(input())
newTemprature = 0
if(operation == 1):
     newTemprature = (temperature-32)*5/9
elif(operation == 2):
    newTemprature = (temperature*9/5)+32

    

if(operation != 1 and operation != 2):  
    print('Wrong Selection')
else:
    print(newTemprature)