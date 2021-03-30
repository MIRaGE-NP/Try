import datetime
current = datetime.datetime.now()
print("Date = ",current.strftime("%Y / %m / %d"))
print("Time = ",current.strftime("%H / %M / %S"))
print("Today is",current.strftime("%A %B %d %Y"))
print(current.strftime("%c"))