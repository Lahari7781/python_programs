from functools import reduce
sales = [
 {"item": "Pen", "price": 10, "qty": 5},
 {"item": "Bag", "price": 500, "qty": 0},
 {"item": "Book", "price": 120, "qty": 3},
 {"item": "Eraser", "price": 5, "qty": 10},
 ]
k=reduce(lambda x,y:x+y,map(lambda x:x['price']*x['qty'],filter(lambda x:x['qty']>0,sales)))
print(k)