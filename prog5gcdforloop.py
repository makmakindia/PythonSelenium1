def gcd(m,n):
    i=min(m,n)
    for j in range(i):
        if (m%j)==0 and (n%/j)==0:
            return j

m = int(input("Enter m value : "))
n = int(input("Enter n value : "))
print(gcd(m, n))