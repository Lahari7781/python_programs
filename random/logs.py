# Use filter() to extract only
# lines that are ERROR level, Each log is in the format "HH:MM
# [LEVEL] message".
logs = [
 "09:15 [INFO] Server started",
 "13:42 [ERROR] Disk full",
 "11:50 [ERROR] Timeout",
 "15:03 [INFO] Request OK",
 "14:20 [ERROR] DB connection lost",
]
fil=list(filter(lambda x:"ERROR" in x,logs))
print(fil)