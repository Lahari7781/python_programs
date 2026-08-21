# 1. Write a custom iterator that prints numbers from 1 to N.
# class num:
#     def __init__(self,n):
#         self.n=n
#         self.start=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if(self.start<=self.n):
#             k=self.start
#             self.start+=1
#             return k
#         else:
#             raise StopIteration
# it=num(20)
# for i in it:
#     print(i)
# 2. Create an iterator that returns only even numbers from a given list.
# class even:
#     def __init__(self,l):
#         self.l=l
#         self.start=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if(self.start<len(self.l)):
#             k=self.l[self.start]
#             if(k%2==0):
#                 self.start+=1
#                 return k
#             else:
#                 self.start+=1
#                 return self.__next__()
#         else:
#             raise StopIteration
# a=even([1,2,3,4,5])
# for i in a:
#     print(i)

# 3. Implement an iterator that iterates over a string character by character in reverse order.
# class res:
#     def __init__(self,k):
#         self.k=k
#         self.start=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start<len(self.k):
#             m=self.start
#             self.start+=1
#             return self.k[m]
#         else:
#             raise StopIteration
# s=res("Hello")
# for i in s:
#     print(i)

# # 4. Write an iterator that yields elements of a list with their index (don’t use enumerate).
# class el:
#     def __init__(self,l):
#         self.l=l
#         self.start=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if(self.start<len(self.l)):
#             k=self.start
#             self.start+=1
#             return self.l[k]
#         else:
#             raise StopIteration
# gen=el([1,2,3,4,5])
# for i in gen:
#     print(i)
# # 5. Write a generator that yields digits from an integer one by one.
# def inti(n):
#     for i in str(n):
#         yield i
# gen=inti(1234)
# for i in gen:
#     print(i)
#
# # 6. Create a generator that yields cumulative sum of numbers in a list. Example: [1,2,3] → 1, 3, 6
# def cum(l):
#     sum=0
#     for i in l:
#         sum=sum+i
#         yield sum
# gen=cum([1,2,3])
# for i in gen:
#     print(i)
# 7. Implement a generator that yields vowels from a string.
def vow(str):
    k=[i for i in str if i in "AEIOUaeiou"]
    yield " ".join(k)
gen=vow("qertunt")
for i in gen:
    print(i)
# 8. Create an iterator that yields words from a sentence one by one.
def sen(sen):
    for i in sen.split(" "):
        yield i
gen=sen("Hello I am Lahari")
for i in gen:
    print(i)
# 9. Write an iterator that returns characters at even indices of a string.
class chr:
    def __init__(self,str):
        self.str=str
        self.start=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<len(self.str):
            k=self.start
            self.start+=1
            if k%2==0:
                return self.str[k]
            else:
                return self.__next__()
        else:
            raise StopIteration
m=chr("qwerty")
for i in m:
    print(i)
# 10. Implement a generator that yields running maximum from a list Example: [3,1,4,2] → 3, 3, 4, 4
def maxi(l):
    maxii=float('-inf')
    for i in l:
        if(i>maxii):
            maxii=i
        yield maxii
m=maxi([3,1,4,2])
for i in m:
    print(i)