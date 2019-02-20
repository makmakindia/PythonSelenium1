
strs1 = 'Chennai'
strs2 = "Hitchhiker's"
strs3 = '''He favorite book is "Hitchhiker's to galaxy!"'''
strs4 = 'Mr\'s Arun \n kumar '
strs5='hello'

print(" Single Quote String : "+strs1)
print("Double quote eString : "+strs2)
print("Triple Quote String : "+strs3)
print("backslash String : "+strs4)
print("String Concatinate : "+strs4+strs1)
print("Slice : "+strs1[1:3])
print("Slice : "+strs3[1:])
print(" Manipulate strings : "+strs5[0:3]+'p!')
print(len(strs1))

"""
String Operations 
+ Concatenation , adds 2 Strings 
len(Str) -- length of string 
Slice -- extracts substring from main string

>>> s1[3]='p'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment


Summary 
Text Values : Type str
Single character is string length 1 
Extract individual char by position 
Slice to extract substrings 
+ glue strings together 
Cannot update strings directly  - immutable 

"""