def compoundInterest(P,R,T):
    return (P*(pow((1+R/100),T)) - P)

principle = 10000
Rate = 10.25
Time = 5

print(compoundInterest(principle,Rate,Time))