#learned how to print multiple lines
#learned to use loop 

import random
a= random.randint(1,20)
print("Lets play a number guessing game!")
print("So, I am guessing a number between 1 to 20")
print("""Your chance starts:
All the best!""")
print()
b=int(input("Enter your guess- "))
if (b==a) :
        print("Excellent! You guessed the correct number.")    
else:
    while(b!=a):
        if  (b>a):
             print("Too high!")
             b=int(input("Enter lesser number- "))
             if (b==a):
                print("Correct Guess!")
             continue
        else:
             print("Too low!")
             b=int(input("Enter greater number- "))
             if (b==a):
                print("Correct Guess!")
             continue


