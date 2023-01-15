text ="Nosotros sabemos Python"
#posiciones[]
print(text[0])

#ultima posicion
print("Ultima posicion")
print(text[-1])
print(text[(len(text)-1)])

#slicing

print(text[0:5]) #sin incluir la ultima
print(text[:16]) #inicio hasta limite
print(text[5:])  #limite hasta el final

#saltos
print(text[:16:2])
print(text[::2])

