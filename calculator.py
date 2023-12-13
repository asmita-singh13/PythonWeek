print("Hello! This calculator is ready for your use. \n Here are the instructions: ")
print("Select 1 for addition")
print("Select 2 for subtraction")
print("Select 3 for multiplication")
print("Select 4 for division")
print("Select 5 for floor division")
print("Select 6 for knowing the remainder")
print("Select 7 for calculating the powers")
print("Select 8 for calculating the roots")
print("Select 9 for calculating roots of quadratic eqn.")
n= int(input("Enter your choice: "))
if n==1 :
    a= int(input("how many parameters you have?"))
    for i in range(0,a):
        c=input("Enter your numbers ")
        b=b+c
    print("The sum is: ", b)
elif n==2:
    a= int(input("Enter the number "))
    b= int(input("Enter the number to be subtracted:"))
    print("The difference is: ", a-b)
elif n==3:
    a= int(input("Enter the multiplicand: "))
    b= int(input("Enter the multiplier: "))
    print("The Product is : ", a*b)
elif n==4:
    a= int(input("Enter the dividend: "))
    b= int(input("Enter the divisor: "))
    print("The division gives: ", a/b)
elif n==5:
    a= int(input("Enter the dividend: "))
    b= int(input("Enter the divisor: "))
    print("The quotient for floor division is: ", a//b)
elif n==6:
    a= int(input("Enter the dividend: "))
    b= int(input("Enter the divisor: "))
    print("The remainder is: ", a%b)
elif n==7:
    a= int(input("Enter the number "))
    b= int(input("Enter the exponent:"))
    print("The required output is: ", a**b)
elif n==8:
    a= int(input("Enter the number "))
    b= int(input("Enter the number for nth root:"))
    print("The required output is: ", a**(1/b))
elif n==9:
    print("The format of eqn is : \n a(x**2) + b(x) + c")
    a= int(input("Enter value of a: "))
    b= int(input("Enter value of b: "))
    c= int(input("Enter value of c: "))
    d= ((b**2) - (4*a*c))**1/2
    a1= (-b + d)/2*a
    a2= (-b - d)/2*a
    print("The required roots are: ", a1  , "and ",  a2)
else :
    print("Invalid choice")

    
