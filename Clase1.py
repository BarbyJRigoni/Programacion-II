# Crear una lista de provincias argentinas
provincias = ["Tierra del Fuego", "Santa Cruz", "Chubut", "Rio Negro", "Neuquen", "Tucumán"]

# Imprimir la lista por pantalla
print(provincias)

print("En la lista de provincias, la segunda es:", provincias[2])

#Imprimir por pantalla del segundo al cuarto elemento

print(provincias[1:4])

#Mostrar el tipo de dato de la lista

print(type(provincias))

#Mostrar los primeros 4 elementos de la lista

print(provincias[0:4])

#Agregar una provincia más a la lista que ya exista y otra que no

provincias.append("Tierra del Fuego")
provincias.append("Salta")

print(provincias)

#Agregar una provincia, pero en la cuarta posición.

provincias.insert(3,"Misiones")

print(provincias)

#Extender otra lista a la ya creada.
provincias2 = ["Buenos Aires"]
provincias.extend(provincias2)
print(provincias)

#Eliminar un elemento de la lista.




#Extraer el último elemento de la lista, guardarlo en una variable e imprimirlo.

#ultima_provincia = provincias(len(provincias-1))

#print("La ultima provincia en la lista es:", ultima_provincia)

#Otro

ultima_prov= provincias.pop()
print(ultima_prov)