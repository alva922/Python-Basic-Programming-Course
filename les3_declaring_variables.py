#In Python, variables are created when you assign a value to it:
x = 5     #integer
y = "Hi!" #string
z=5.1     #float
zz = 1j   # complex
bl=False  #boolean 
print(bl)
#False
print(x)
#5
print(y)
#Hi!
print(z)
#5.1
print(zz)
#1j
print(type(bl))
print(type(x))
print(type(y))
print(type(z))
print(type(zz))
#<class 'bool'>
#<class 'int'>
#<class 'str'>
#<class 'float'>
#<class 'complex'>
#You can convert from one type to another with the int(), float(), and complex() methods
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#1.0
#2
#(1+0j)
#<class 'float'>
#<class 'int'>
#<class 'complex'>
