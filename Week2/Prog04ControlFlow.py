"""
Control Flow -> determines order in which statements are executed

1. Conditional Execution
2. Repeated Exeution - Loop
3. Function Definition

- if(m%2)==0:

- if(m%2)==0:
  else:

-- if(m%2)==0:
    elif:

-- for i in [1,2,3,4]:

-- for i in range(1,10):



"""

def factors(n):
    flist = []
    for i in range(1,n+1):
        if n%i == 0:
            flist = flist+[i]
    return flist


n = int(input("Please Enter the First Value n: "))
print(factors(n))