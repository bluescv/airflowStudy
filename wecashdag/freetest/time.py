import datetime
#获得当前时间
now = datetime.datetime.now()
print(now)
#转换为指定的格式:
otherStyleTime = now.strftime("%Y-%m-%d%H:%M:%S")
otherStyleTime = now.strftime("%Y%m%d%H%M%S")

print(otherStyleTime)