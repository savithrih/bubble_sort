import random
import datetime
start = datetime.datetime.now()
list=[]
for i in range(0,5):
 num = random.randint(0,1000)
 num_value = int(round(num))
 list.append(num_value)
for z in range(0,len(list)):
 min = z
 for j in range(z+1,len(list)):
  if list[j]<list[min]: 
   min = j
 # if j!= z:
   temp = list[z]
   list[z] = list[min]
   list[min] = temp
print list
end = datetime.datetime.now()
print "starttime is",str(start) +"\n","endtime is", str(end)