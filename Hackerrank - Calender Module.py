import calendar
MM, DD, YY = map(int, input().split())
print((calendar.day_name[calendar.weekday(YY, MM, DD)]).upper())