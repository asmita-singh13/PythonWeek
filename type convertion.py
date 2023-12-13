#converting one data type into another is type casting or type convertion
# by default lower order is converted into higher order to prevent data loss

a=5
print(type(a))
b=3.2
print(type(b))
# it will give float output_ bydefault (implicit type conversion)
print(a+b)
print(type(a+b))

#for integer_ we need to tell computer to covert into desired type (explicit type conversion)
c=a+b
print(int(c))



x="1"
print(type(x))
y="6"
print(x+y)
print(type(x+y))

#now converting string to int because the string contains valid integer
# while "hello" cannot be converted to int as it is not a valid integer

print(int(x)+ int(y))
print(type(int(x)+ int(y)))

z="asmi"
#print(int(z)) #this line will give error!