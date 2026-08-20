# # class A:
# #     def __init__(self,start,end):
# #         self.start=start
# #         self.end=end
# #     def __iter__(self):
# #         return self
# #     def __next__(self):
# #         if self.start<=self.end:
# #             self.start+=1
# #             return self.start-1
# # a1=A(1,25)
# # print(next(a1))
# # for i in a1:
# #     if i is None:
# #         raise StopIteration
# #     print(i)
#
# class list_iter:
#     def __init__(self,l):
#         self.l=l
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<len(self.l):
#             self.index += 1
#             if(self.l[self.index-1]%2==0):
#                 return self.l[self.index-1]
#             else:
#                 return self.__next__()
#         else:
#             raise StopIteration
#
# l=list_iter([1,2,3,4,5,6,7,8,9])
# for i in l:
#     print(i)
# class A:
#     def __init__(self):
