from datetime import datetime

def calculate_days_between(start_date, end_date):
    start_date = datetime.strptime("2024-10-10", '%Y-%m-%d')
    end_date = datetime.strptime("2024-12-31", '%Y-%m-%d')
    delta = end_date - start_date
    return delta.days
print(calculate_days_between("2024-10-10", "2024-12-31"))

