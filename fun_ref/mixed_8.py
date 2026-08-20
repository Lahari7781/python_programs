# Q8.  FULL PIPELINE: Build a mini data pipeline. Start with a list of student dictionaries [{name, score}]. Use filter() to keep scores >= 60
# , map() to add a 'grade' key ('Pass'), and sorted() to sort by score descending. Print the final result
k={"lahari":100,"Madhuri":60,"sand":25}
l=dict(filter(lambda x:x[1]>=60,k.items()))


