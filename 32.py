tup = [("c",3),("f",6),("d",4),("a",1),("b",2),("e",5)]

for i in range(0,len(tup)):
    for j in range(0,len(tup)-1):
        if tup[j] > tup[j+1]:
            temp = tup[j]
            tup[j] = tup[j+1]
            tup[j+1] = temp

print(tup)
        
         
        