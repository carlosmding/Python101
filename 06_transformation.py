#cambio dinamico de la variable
name = "Carlos"
print(type(name))
name = 12
print(type(name))

#transformacion
# usando str()
edad = 30

print("Mi edad es " + str(edad))
print(f"Mi edad es {edad}")

#input siempre recibe en str
edad = input("Escribe su edad por favor: ")
print(type(edad))
edad = int(edad) + 10
print(f"Tu edad en 10 años serian {edad} años")