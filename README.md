# break-time
Take a break - A python script which opens up your browser every 2 hours (or however long you set the time to)

```
import time
import webbrowser

TOTAL_BREAKS = 3
BREAK_COUNT = 0

print("This program started on" + time.ctime())
while (BREAK_COUNT < TOTAL_BREAKS):
    # Change time to how often you want the browser to open
    time.sleep(2*60*60)
    # Place any URL below
    webbrowser.open("https://www.youtube.com/watch?v=j5-yKhDd64s")
    BREAK_COUNT = BREAK_COUNT + 1
```
