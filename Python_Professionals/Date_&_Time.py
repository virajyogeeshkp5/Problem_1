# Date and Time
#from datetime import datetime, timedelta, timezone
#JST=timezone(timedelta(hours=+9)) 

#dt= datetime(2015,1,1,12,0,0,tzinfo=JST)
#print(dt)

# Today print date and time 
from datetime import datetime, timedelta
now=datetime.now()
print(now)
then=datetime(2024,11,15)
print(then)

delta = now-then
print(delta.days)

print(delta.seconds)

import datetime

# Date Object
today=datetime.date.today()
print(today)

now=datetime.datetime.now()
print(now)

import datetime
today=datetime.date.today()
print('Today:',today)

yesterday=today-datetime.timedelta(days=1)
print('yesterday:',yesterday)

tomorrow=today+datetime.timedelta(days=1)
print('tomorrow:',tomorrow)

print('difference between yesterday and tomorrow:',yesterday-tomorrow)


# Enum
from enum import Enum
class colour(Enum):
    red=1
    green=2
    blue=3

print(colour.red)

print(colour(1))


print(colour['red'])


print([c for c in colour])
