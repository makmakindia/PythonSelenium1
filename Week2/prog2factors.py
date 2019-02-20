def factor(n):
    flist=[]
    for i in range(1,n+1):
        if n%i == 0:
            flist=flist+[i]
    return flist

n = int(input("Enter n value : "))
n1 = factor(n)
print(n1)