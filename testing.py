from datetime import time
import datetime


# function to get the date and time
def day_and_time():
    now = 2022-03-17 13:29:06
    print(now)
    # now = "2022-03-17 13:29:06"
    t = now.strftime('%H:%M:%S')
    if int(t[0:2]) > 12:
        clk = " PM"
    else:
        clk = " AM"
    dt = [now.strftime("%B %d, %Y"), t, clk]
    return dt


dat = day_and_time()
# print(dat)
