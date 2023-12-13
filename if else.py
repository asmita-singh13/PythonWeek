import time
currentTime = time.strftime('%H:%M')   
hour = int(time.strftime('%H'))
if (currentTime.hour) < 12 :
     print('Good morning')
if (currentTime.hour) > 12 :
     print('Good afternoon')
if (currentTime.hour) > 6 :
     print('Good evening')
    