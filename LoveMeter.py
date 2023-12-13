#using random module to make a funny love calculator!
#here random is built in module
#it generates random number on its own

import random as r
a=input("Enter your name: ")
b=input("Enter your partner's name: ")
c= r.randint(1,100)
if c in range (0,50):
    print("Not compatible couple!")
    print("Try again")
    print ("Your love score is: ",c)
elif c in range (50,80):
    print("Move ahead, make efforts!")
    print("There are chances of some great chemistry!")
    print("Wish you luck!")
    print("Your love score: ", c)
else:
    print("Rab ne bna di jodi...")
    print("Things are in your favour!")
    print("Your love score: ",c)
    