import time
import datetime
current_time = datetime.datetime.now()
print("Current day: ", current_time.day)
print("Current hour: ", current_time.hour)
print("Current minutes: ", current_time.hour * 60)
print("Current seconds: ", current_time.minute * 60)

seconds = time.time()
minutes = seconds / 60
hours = minutes / 60
days = hours / 24
print("days since epoch :", days)
