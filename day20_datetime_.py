
import calendar
print(calendar.month(2026,7))
print(calendar.prcal(2026))


import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
st = "Esha Verma"
for s in st:
    print(s)
    time.sleep(1)
    
from datetime import datetime as dt 
print(datetime.datetime(2026,7,14,8,42,30))

if dt(dt.now().year,
      dt.now().month,
      dt.now().day,
      8) < dt.now() < dt(dt.now().year,
                          dt.now().month,
                          dt.now().day,
                          16):
    print("Working hours....")
else:
    print("Fun hours")

