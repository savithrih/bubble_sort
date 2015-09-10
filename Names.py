users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
# for key,data in users.items():
#  print key
#  for value in data:
for index,value in enumerate(Students,start=1):
 print key
 print enumerate(index),"-"+value["first_name"]," ",value["last_name"],"-",len(value["first_name"])+len(value["last_name"])
  