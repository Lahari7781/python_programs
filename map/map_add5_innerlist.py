# # # # # # Use map() with a lambda to add 5 to every element of the following
# # # # # # nested list [[1, 2], [3, 4], [5, 6]]
# # # # # l=[[1,2],[3,4],[5,6]]
# # # # # k=list(map(lambda x: list(map(lambda y:y+5,x)),l))
# # # # # print(k)
# You have a list of server log strings. Use filter() to extract only
# lines that are ERROR level, Each log is in the format "HH:MM
# [LEVEL] message".
logs = [
 "09:15 [INFO] Server started",
 "13:42 [ERROR] Disk full",
 "11:50 [ERROR] Timeout",
 "15:03 [INFO] Request OK",
 "14:20 [ERROR] DB connection lost",
]
f=list(filter(lambda x:"ERROR" in x,logs))
print(f)
