"""
Fucntions

"""

def powernm(n,m):
    ans = 1
    for i in range(0,n):
        ans = ans*m
    return ans


n = int(input("Enter Value for n : "))
m = int(input("Enter Power Value for m : "))

print(powernm(n,m))

