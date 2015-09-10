import datetime
import random
start = datetime.datetime.now()
list =[]
for j in range(0,10):
 num = random.randint(1,10)
 list.append(num)
 for i in range(0,len(list)):
  for z in range(0,len(list)-1):
   if list[z]>list[z+1]:
     (list[z+1],list[z])=(list[z],list[z+1]);
 print list
end = datetime.datetime.now()
print "starttime is",str(start) +"\n","endtime is", str(end)

