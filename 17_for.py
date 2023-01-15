my_list = [1, 5,6,87,56,21,4,6,82] #listas y tuplas

for element in my_list:
  print(element )

personas = [
  {
  "id" : "1232", 
  "nombre": "camisa", 
  "total": 10 
  },
  {
  "id" : "345", 
  "nombre": "camisita", 
  "total": 15 
  },
  {
  "id" : "987", 
  "nombre": "pant", 
  "total": 18 
  },
]
"""
for i in person: #itera las llaves
  print(i)

for i in person: #itera las valores
  print(person[i])

for key, value in person.items():
  print("key => ", key, " valor=> ", value)
"""
# Listas de diccionarios
for person in personas:
  print("id=> ",person["total"])



  
