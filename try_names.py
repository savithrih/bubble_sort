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
student_dic = users["Students"]
for index,value in enumerate(student_dic,start=1):
 # for key,data in users.items():
 #  print list(dict.keys())[0]
 print index,"-",value["first_name"]," ",value["last_name"],"-",len(value["first_name"])+len(value["last_name"])
instructors_dic = users["Instructors"]
for index,value in enumerate(instructors_dic,start=1):
 print index,"-",value["first_name"]," ",value["last_name"],"-",len(value["first_name"])+len(value["last_name"])
