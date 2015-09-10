# def bubble_sort():
#  temp =0
#  for j in range(0,100):
#   for i in range(0,99):
#    if a[i]> a[i+1]:
#   	temp = a[i]
# 	a[i]=a[i+1]
# 	a[i+1]=temp
#  return a
import datetime
import random
list =[]
for j in range(0,10):
 num = random.randint(1,10)
 list.append(num)
 for i in range(0,len(list)):
  for z in range(0,len(list)-1):
   if list[z]>list[z+1]:
     (list[z+1],list[z])=(list[z],list[z+1]);
 print list
	 
