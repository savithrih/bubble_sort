x = [14,"savi","DFdsf"]
for i in range(0,len(x)):
 if type(x[i])is str:
  print x[i][0] * len(x[i])
 if type(x[i]) is int:
  print x[i]* "*"



