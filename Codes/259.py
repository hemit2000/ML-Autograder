import datetime

def convert_datetime_to_timestamp(date_time, timestamp_format):
    dt = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
    return dt.strftime(timestamp_format)

date_time = "2020-05-02 15:30:00"
timestamp_format = "%Y/%m/%d %H:%M:%S"
result = convert_datetime_to_timestamp(date_time, timestamp_format)
print(result)
