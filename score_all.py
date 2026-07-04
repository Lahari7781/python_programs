students = [
 {"name": "Ravi", "score": 45},
 {"name": "Sneha", "score": 78},
 {"name": "Kiran", "score": 60},
 {"name": "Divya", "score": 92}
]
# 1. Keep students with score >= 60
# 2. Add a "grade": "Pass" key to each
# 3. Sort the result by score, descending and finally print the result
fil=list(filter(lambda x:x['score']>=60,students))
m=list(map(lambda x:x|{"grade":"pass"},fil))
s=sorted(m,key=lambda x:x["score"],reverse=True)
print(s)