# -*- coding: utf-8 -*-

import datetime

date = datetime.datetime(1901,1,1,12,0,0)

count = 0

while date.year != 2001:
    if date.weekday() == 6 and date.day == 1:
        print(count)
        count += 1
    date += datetime.timedelta(days=1)

