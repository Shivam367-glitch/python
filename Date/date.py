import datetime

print(dir(datetime))
print(datetime.MAXYEAR)
print(datetime.MINYEAR)
print(datetime.time())
print(datetime.timedelta())

print(datetime.tzinfo)
print(datetime.UTC)

print(datetime.datetime.now())

# to get today date and time 
x=datetime.datetime()
print(x.strftime("%d%m/%Y"))
print(datetime.datetime.now().date())





