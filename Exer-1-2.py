# seconds
totalSeconds = (42 * 60) + 42
print("total seconds : ", totalSeconds)
total_min = totalSeconds / 60
# miles
miles = 10 / 1.61
print("Total miles : ", miles)
# avg pace
print("avg pace in sec: ", totalSeconds / miles)
print("avg pace in min: ", total_min / miles)
# mph
hour = total_min / 60
print("mph: ", miles / hour)