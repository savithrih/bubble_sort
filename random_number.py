import random
head_value =0;
tail_value =0;
for element in range(0,5):
 num =random.random()
 final_num=round(num)
 if final_num == 0.0:
  tail_value+= 1
  print "Attempt#"+str(element)+":Throwing a coin..It's tail..Got"+str(tail_value)+"head(s) and"+str(head_value)+"tail(s) so far" 
 elif final_num == 1.0:
  head_value+= 1
  print "Attempt#"+str(element)+":Throwing a coin..It's head..Got"+str(tail_value)+"head(s) and"+str(head_value)+"tail(s) so far" 
print "Ending the program,thank you!"

