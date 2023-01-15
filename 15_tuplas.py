numbers = (1,2,3,4,5,1,2,3)
strings = ("hi", "konnichiwa", "sowadi")

print(type(numbers))

#CRUD
# No se puede agregar
print(numbers.index(2))
print(numbers.count(2))

#tuplas no se pueden cambiar
#se pasa como lista
print(numbers)
my_list = list(numbers)
print(my_list)

#retornar a tupla
my_list[0] = 99
my_tupla =  tuple(my_list)
print(my_tupla)
