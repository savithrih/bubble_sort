import random
import datetime
start = datetime.datetime.now()
list=[]
for a in range(0,100):
 num = random.randint(0,1000)
 num_value = int(round(num))
 list.append(num_value)
for i in range(0,len(list)):
 for j in range(i,0,-1):
  if list[j]<list[j-1]:
  	temp = list[j]
  	list[j]=list[j-1]
  	list[j-1] =temp
  else:
  	break
print list
end = datetime.datetime.now()
print "starttime is",str(start) +"\n","endtime is", str(end)