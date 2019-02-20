def gcdEuclid(m,n):
    if(m>n):
        (m,n)=(n,m)

    while(m%n)!=0:
        diff=m-n
        (m,n)=(max(m,diff),min(n,diff))

        return n


m = int(input("Enter m value : "))
n = int(input("Enter n value : "))
print(gcdEuclid(m,n))
