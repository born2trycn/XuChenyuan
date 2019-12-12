import time
now = time.gmtime()
print(now)

month = now.tm_mon
day = now.tm_mday

print(month)
print(day)

if (month == 8):
    if (day == 22):
        print('我的生日')
if (month == 5):
    if (day == 10):
        print('爹的生日')
    elif (day == 9):
        print('老弟的生日')
if (month == 12):
    if (day == 7):
        print('某人的生日')
if (month == 6):
    if (day == 21):
        print('父亲节快乐')
if (month == 5):
    if (day == 10):
        print('母亲节快乐')