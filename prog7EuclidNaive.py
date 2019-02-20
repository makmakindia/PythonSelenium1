def gcdEuclidAdv(m,n):
    if m>n:
        (m,n)=(n,m)

    if(m%n) == 0:
        return n;
    else:
        return gcdEuclidAdv(n,m%n)


m = int (input("Enter m value : "))
n = int (input("Enter n value : "))
print(gcdEuclidAdv(m,n))