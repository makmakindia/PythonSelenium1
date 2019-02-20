"""def f(x):
    d=0
    while x >= 1:
        (x,d) = (x/4,d+1)
    return d


K = int(input("Enter value for K : "))
print(f(K))
"""
"""def h(n):
    s = 0
    for i in range(1,n):
        if n%i == 0:
            s = s + i
          # print(i)
          # print(n%i)
    return(s)


n1 = int(input("Enter n1 value : "))
print(h(n1))
print(28-13)
"""

# 3. For what value of n would g(47,n) return 5?
def g(m,n):
    res = 0
    while m >= n:
        (res,m) = (res+1,m-n)
    return(res)


m1 = int(input("Enter m1 value : "))
n1 = int(input("Enter n1 value : "))
print(g(m1,n1))