from datetime import datetime

def day_of_week(date):
    # convert string to date object
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    # retrieve weekday
    day = date_obj.strftime("%A")
    return day

print(day_of_week("2020-12-25"))
