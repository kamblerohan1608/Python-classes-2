# Built in libraries :-     1. Modules : time,os,sys,random
#                           2. Packages : numpy,pandas,matplotlib

import time
a= time.time()
print("The time is ",time.strftime('%I:%m:%S'))
print("The date is ",time.strftime('%d - %M - %y'))
#help(time.strftime)
b=time.time()

print((b-a)*1000)