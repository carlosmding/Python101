text ="Ella sabe programar en Python"

#in
print("ella" in text)
if "ella" in text:
  print("Perfecto")
else:
  print("no estaba")

#len, tamaño número caracteres
print (len(text))

#upper and lower
print(text.upper())
print(text.lower())

#count
print(text.count("a"))

#swapcase cambio may por min y viceversa
print(text.swapcase())

#startwith and endswith
print(text.startswith("Ella"))
print(text.endswith("Python"))

#replace
print(text.replace("Ella", "Nosotros"))

#capitalize and title
print(text.title())

#isdigit
print("245".isdigit())