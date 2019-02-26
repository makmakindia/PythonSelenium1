

def factors(n):
    flist = []
    for i in range(1,n+1):
        if n%i == 0:
            flist = flist + [i]
    return flist


def isprime1(n):
    return(factors(n) == [1,n])


def primesupto(n):
    plistupto = []
    for i in range(1,n):
        if isprime1(i):
            plistupto = plistupto + [i]
    return plistupto;


n = int(input("Enter value of n to find factors : "))
print(factors(n))
print(str(n)+" is a Prime  ? : ")
print(isprime1(n))
print("List of prime values : ")
print(primesupto(n))


