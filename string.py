#string can be enclosed between single our double quotes
#string is the sequence of array of textual data 
#it is used when working with unicode characters
name="asmi"
friend= 'noddy'

#sometimes we need to print quotes in strings so we can-
print('he says, "Hello!"')
print("he says,\"how are you?\" ")

#multiple line string
c= '''hi 
i am 19 yrs old
how u doing?'''

#indexing starts from 0 to n-1
print(name[0])
print(name[1])

#iteration
print("Lets run a loop")
for character in c:
    print(character)

#string slicing
#variable[0:n]
#0= start, n= stop. Last value will be n-1
#len() function gives length
l1= len(friend)
print(l1)
print(friend[0:2])
print(friend[1:3])
print(friend[:])
print(name[0:-2])
print(name[-1:-2]) #no ans; blank as len-1:len-2, [3:2] no sense
print(name[-2:-1]) #it will give ans as [2:3]

#strings are immutable
#METHODS:
print(name.upper())
print(name.lower())
#strip removes trailing character
abc="uigihji......."
print(abc.rstrip("."))
xyz="....abc"
print(xyz.lstrip("."))
print(abc.strip("."))
print(xyz.replace("abc", "xyz"))
print(abc.split("i"))
head= "intro tO Py"
print(head.capitalize()) # capitalize convert 1st letter to capital and all to small
print(abc.count("i"))
print(abc.center(20))
print(abc.endswith("..."))
#returns boolean value
print(abc.endswith("ghjjg"))
print(abc.endswith(".",4,10)) #tells that in given substring do it ends with a "."
print(abc.find("i")) #return the index of the element found in 1st place, rest well be ignored
#index() is same as find() but find return -1 if element not found. But index() will give error
# isalnum() - it consists of A-Z, a-z, 0-9 ; returns true or false
# isalpha() - it consists of A-Z, a-z ; returns true or false
# islower()
# isupper()
# isprintable()- if we have escape sequence, then false
# isspace()
ab=" hi, ria."
print(ab.isspace()) # it should only contain space or tab. ab returns false because it has characters too
# istitle() - all 1st letters of words must be capital
# startswith("hjh")- return if it starts with it or not, we can even give index like endswith
# swapcase()- upper to lower and lower to upper!
# title()- convert in title case