class power:
    def pow(a,b):
        if b == 0:
            return 1
        else:
            while b > 0:
                return pow(a, b-1)
            


print(pow(2,6))