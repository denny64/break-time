# Break Time
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

# Rename Files
A mini python script to help you rename files. It currently removes all numbers from file names, but can be easily adjusted to suit your needs

```
import os

def rename_files():
    file_list = os.listdir("/Users/dennyvuong/Desktop/python_foundations/prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir("/Users/dennyvuong/Desktop/python_foundations/prank")

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "1234567890")) # <-- replace the string to anything you want to remove from the file name
    os.chdir(saved_path)
    print(file_list)

rename_files()

```
