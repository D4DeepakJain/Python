def check(str):
    a = 0
    strv = 'aeiou'
    vowels = set(strv)
    for i in vowels:
        if i in set(str.lower()):
            a= a +1
    
    if a==5:
        print('Accept')
    else:
        print('Not Accept')


check(input())