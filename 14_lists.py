numbers = [1,5,6,8,7,1,2,5]
print(numbers, type(numbers))

#difeentes tipos
types=["hola", 3, [1,2,3], 5.3]
print(type(types[0]))

#mutaciones
#string no son mutables 

types[0] = "nueva cadena"
print(types)

print(3 in types)

#métodos de listas CRUD
# Create, Read, Update and Delete

types.append(700) #ingresar al final
print(types)

types.insert(0, "Holitas") #inserta y corre los otros elementos
print(types)

new_list = types + numbers
print(new_list)

#posicion index
new_list[new_list.index("nueva cadena")] = "Cadenota"
print(new_list)

#eliminar
new_list.remove("Holitas")
new_list.remove("Cadenota")
print(new_list)

new_list.pop() #remover el ultimo elemento o si le doy una posicion este lo elimina
print(new_list)

#reverse
numbers.reverse()
print(numbers)

#ordenar tanto numeros como letras del mismo tipo
numbers.sort()
print(numbers)




