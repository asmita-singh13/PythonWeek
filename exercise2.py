import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
ho = int(time.strftime('%H'))
#print(ho)
mine = int(time.strftime('%M'))
#print(mine)
scnd = int(time.strftime('%S'))
#print(scnd)
if ho >=5 :
    if ho <=11 :
        if mine <= 59:
            if scnd <=59:
                print("Good morning!")
elif ho >=12:
    if ho<=16 :
        if mine <= 59:
            if scnd <=59:
                print("Good afternoon!")
elif ho >=17:
    if ho <=20 :
        if mine <= 59:
            if scnd <=59:
                print("Good evening! ")
else:
    print("Good night!")