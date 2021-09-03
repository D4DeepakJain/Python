def myfun(arr,n):
    mul =1
    for i in range(arr):
        mul = mul * (i % n)
    return mul % n
        



aa = [9,2,4,4,8,4,5,5,]

print(myfun(aa, 3))