milliseconds = 10000123
seconds = milliseconds // 1000
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds2 = seconds % 60

MilliSeconds = milliseconds % seconds



print(milliseconds)
print(hours)
print(minutes)
print(seconds2)
print(MilliSeconds)