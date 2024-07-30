import datetime

def get_day_of_week(date):
    year, month, day = map(int, date.split('-'))
    day_of_week = datetime.date(year, month, day).weekday()
    return day_of_week + 1

print(get_day_of_week("2020-05-15"))
