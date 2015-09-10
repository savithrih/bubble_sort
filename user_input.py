def grade(user_value):
  print user_value
  if user_value >= 60 and user_value <= 69:
   print "Score: %s; Your Grade is D" % user_value
  elif user_value >= 70 and user_value <= 79:
   print "Score: %s; Your Grade is C" % user_value
  elif user_value >= 80 and user_value <= 89:
   print "Score: %s; Your Grade is B" % user_value
  elif user_value >= 90 and user_value <= 99:
   print "Score: %s; Your Grade is A" % user_value
  else:
   print "Score: %s; User Failed" % user_value
for i in range(0,11):
 user_value = input("Enter the input")
 grade(user_value)
print "End of the program.Bye!"
 

