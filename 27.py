def rem(lst):
    for num in lst:
        if num < 0:
            lst.remove(num)
            
a = [4,-5,7,-3,2,5,534,6,-56,65,64,-6,6,-64,4,4,-6,7,-8,8,3,2,13,-31,-67,2,0]
rem(a)
print(a)
