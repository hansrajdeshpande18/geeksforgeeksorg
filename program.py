import calendar
#create a plain text calendar
c =calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2021, 3)
print(str)
print("names of the months in the year")
for name in calendar.month_name:
    print(name)
print("Names of the days in a week:")
for day in calendar.day_name:
    print(day)