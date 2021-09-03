def cubesum(n):
    sum = 0
    for i in range(n+1):
        sum += i*i*i
    return sum

a = int(input('Enter number'))
print(cubesum(a))


