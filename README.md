# break-time
Take a break - This program will open your browser every 2 hours to make you take a break

import time
import webbrowser

TOTAL_BREAKS = 3
BREAK_COUNT = 0

print("This program started on" + time.ctime())
while (BREAK_COUNT < TOTAL_BREAKS):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=j5-yKhDd64s")
    BREAK_COUNT = BREAK_COUNT + 1
