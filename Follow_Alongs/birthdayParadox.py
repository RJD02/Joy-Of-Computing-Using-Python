import random
import datetime

birthday = []
i = 0
while(i < 10):
    year = random.randint(1899, 2021)
    # The oldest person to ever live was 122 years old, and we are shortening our life span, so 122 must be good enough.
    if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        leap = 1
    else:
        leap = 0
    month = random.randint(1, 12)
    if month == 2 and leap == 1:
        day = random.randint(1, 29)
    elif month == 2 and leap == 0:
        day = random.randint(1, 28)
    elif month == 7 or month == 8:
        day = random.randint(1, 31)
    elif month % 2 != 0 and month < 7:
        day = random.randint(1, 31)
    elif month % 2 == 0 and month > 7 and month < 12:
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)
    dd = datetime.date(year, month, day)
    day_of_year = dd.timetuple().tm_yday
    i = i + 1
    print(i)
    birthday.append(day_of_year)

birthday.sort()
i = 0
while(i < 10):
    print(birthday[i])
