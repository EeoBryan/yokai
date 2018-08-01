import webbrowser
import time

#after 2hrs will prompt user to take a break

total_breaks = 3
break_count = 0

print("Program has started at: " + time.ctime())
while(break_count < total_breaks):
    time.sleep(10) #7200 for 2hrs
    webbrowser.open(r"D:/Python27/pythonProjs/breakTime/index.html")
    #r here stands for rawpath, it will tell python to take everything as it is
    break_count = break_count + 1
