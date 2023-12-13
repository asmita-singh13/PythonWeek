# here we have made a dynamic counting system
# here we did iteration with for loop 
# if is also used for checking the condition

print("We have a voting for selection of class representative!")
print("There are 3 nominations:")
print("Type '1'  to vote for ARYAN." )
print("Type '2'  to vote for ASMITA." )
print("Type '3'  to vote for GAGAN." )
print("Any other entry than 1,2 or 3 will be considered as WRONG input"  )
a= int(input("Enter the number of voters: "))
a1=0
a2=0
a3=0
a4=0
for i in range (0,a):
    p= int(input("Your vote: "))
    if p==1 :
        a1=a1+1
    elif p==2:
        a2=a2+1
    elif p==3 :
        a3=a3+1
    else:
        a4=a4+1

print(''' RESULTS are as follows: ''')
print("CANDIDATE  : SCORE")
print("ARYAN  : ", a1)
print("ASMITA : ", a2)
print("GAGAN  : ", a3)


    