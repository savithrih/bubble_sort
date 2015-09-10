import random
import datetime
start = datetime.datetime.now()
list=[]
for i in range(0,10):
 num = random.randint(0,1000)
 num_value = int(round(num))
 list.append(num_value)
print list
for z in range(0,len(list)/2+1):
 min = z
 max = len(list)-z-1
 for j in range(z+1,len(list)-z):
  if list[j]<list[min]: 
   min = j
  if list[j]>list[max]:
    max = j
 if min!= z:
  temp = list[z]
  list[z] = list[min]
  list[min] = temp
 if max!=len(list)-z-1:
  temp = list[len(list)-z-1]
  list[len(list)-z-1] = list[max]
  list[max] = temp
print list
end = datetime.datetime.now()
print "starttime is",str(start) +"\n","endtime is", str(end)