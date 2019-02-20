def gcd(m,n):
    cf=[]
    for i in range(1, min(m,n)+1):
        if(m%i) == 0 and (n%i) == 0:
            cf.append(i)
    return cf[-1]


m = int(input("Enter m value : "))
n = int(input("Enter n value : "))
print(gcd(m,n))
