
list1 = [1,3,5,6]
print(list1)
list2 = list1
print(list2)

# Add values to list
list1.append(10)
print(list1)
# Remove value from list
list1.remove(10)
print(list1)

list1.append(30)
print(list1)

if 30 in list1:
    list1.remove(30)
print(list1)

# extend list with list of values
l3 = [901,902]
list1[2:] = [100,101,102]
list1.extend(l3)
print(list1)
print(list2)

#reverse list in place
list1.reverse()
print(list1)

#list sort
list1.sort()
print(list1)

#list index
print(list1.index(101))

def factor(n):
    flist = []
    for i in range(1,n+1):
        if n%i == 0:
            flist.append(i)
    return flist


n = int(input("Enter value for find factors : "))
print(factor(n))
