for i in range(2,21):
    flag = False
    for j in range(2,i):        
        if(i % j) == 0:
            flag = True
            break
    if (flag == False):
            print(i)
        
