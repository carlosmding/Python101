name= "Carlos"
last_name="Pinto"
edad="20 años"

full_name = name + " " + last_name
print(full_name)

#quote
#Usando comillas sencillas o doble
quote= "I´m so clever" 
print(quote)

#format
template="Hola, mi nombre es "+ name + " y mi aplellido es "+ last_name
print(template)

template="Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print(template)

template= f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print(template)

template= f"Hola, mi nombre es {full_name} y mi edad es {edad}"
print(template)
