from datetime import datetime as dt
# Get the current time, returns a value like 2022-10-09 17:46:45.151666
today = dt.now()
print(today)
# Get Unix time, returns a value like 1665566809.057217
unix_epoch_time = dt.timestamp(today)
print(unix_epoch_time)

weekday = dt.now().strftime("%A") 
month = dt.now().strftime("%B")
day = dt.now().strftime("%C")
hour = dt.now().strftime("%D")