
# take a list and sort it in assending order without using any built in method or function

ls = [15,1,14,2,13,3,12,4,11,5,10,6,9,7,8,10]

# def sorting(ls,reverse = False):
#     ls = ls
#     if reverse == False:
#         for i in range(len(ls)):
#             for j in range(i+1,len(ls)):
#                 if ls[i] > ls[j]:
#                     ls[i],ls[j] = ls[j],ls[i]
#     if reverse == True:
#         for i in range(len(ls)):
#             for j in range(i+1,len(ls)):
#                 if ls[i] < ls[j]:
#                     ls[i],ls[j] = ls[j],ls[i]
#     return(ls)

# print(sorting(ls,reverse = True))

# ls.sort(reverse=True)
# print(ls)

ls[0] = 100
print(ls)