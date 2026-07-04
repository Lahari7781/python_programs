li=['cat', 'elephant', 'dog', 'rhinoceros']
from functools import reduce
r=reduce(lambda x,y :x if len(x)>len(y) else y,li)
print(r)