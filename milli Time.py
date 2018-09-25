import time
import calendar

def Clock():

    seconds = calendar.timegm(time.gmtime())
    current_second = seconds % 60
    minutes = seconds // 60
    current_minute = minutes % 60
    hours = minutes // 60
    current_hour = hours % 24

    return current_hour, current_minute, current_second

x = True
while x == True:
   h, m, s = Clock()
   time.sleep(1)
   print(h,":",m,":",s)
