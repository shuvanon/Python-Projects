import time
import webbrowser

total_breaks = 3
break_count = 0

print ("This program started on"+time.ctime())

while(break_count<total_breaks):
    time.sleep(60*20)
    webbrowser.open('https://www.facebook.com')
    break_count=break_count+1
print ("This program done on"+time.ctime())
