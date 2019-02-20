'''
x = [1,"abcd",2,"efgh",[3,4]]  # Statement 1
print(x)
y = x[0:50]                    # Statement 2

z = y
x[1] = x[1][0:3] + 'd'
y[2] = 4
z[0] = 0
x[1][1:2] = 'yzw'
'w[4][0] = 1000
'a = (x[4][1] == 4)
print(x[1][1:2])# Statement 3
w = x                          # Statement 4
        # Statement 5
                       # Statement 6
                       # Statement 7
x[1][1:2] = 'yzw'              # Statement 8
               # Statement 9
a = (x[4][1] == 4)             # Statement 10


x = ['a',42,'b',377]
w = x[1:]
y = x
u = w
w = w[0:]
w[0] = 53
x[1] = 47
print(x[1])
print(y[1])
print(w[0])
print(u[0])

first = "wombat"
second = ""
for i in range(len(first),0,-1):
  second = first[i-1] + second


print(second)
'''
def mystery(l):
  l = l[2:5]
  return()

list1 = [7,82,44,23,11]
mystery(list1)

print(list1)
