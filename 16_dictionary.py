my_dict = {}

my_dict = {
  "name" : "Pepito",
  "id" : "123456",
  "edad" : 25
}

print(my_dict)
print(len(my_dict))

print(my_dict["id"])

#usar el .get permite retornar un None si no existe

print(my_dict.get("otro"))
print(my_dict.get("id"))

print("name" in my_dict)

#métodos
my_dict["name"] = "Pepitos mucho"

my_dict["edad"] += 10
print(my_dict)

del my_dict["name"]
my_dict.pop("id") #requiere una posicion para hacer la función
print(my_dict)

#traer los ítems, keys y valores
print(my_dict.items()) #devuelva los pares clave valor en una tupla

print(my_dict.keys()) 

print(my_dict.values())


