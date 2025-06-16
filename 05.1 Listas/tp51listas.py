#Actividad 1
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

#Actividad 2
gustos = ["chocolate", "pizza", "hamburguesas", "gatos", "música"]
print(gustos[-2])  


#Actividad 3
lista_vacia = []
lista_vacia.append("perro")
lista_vacia.append("gato")
lista_vacia.append("tortuga")
print(lista_vacia)

#Actividad 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#Actividad 5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#El programa crea una lista llamada numeros con los valores [8, 15, 3, 22, 7]
#Se busca el valor maximo de la lista con max(numero) que es el valor 22.
#Se elimina el valor 22 de la lista con remove() y luego se imprime la lista,
#que nos volvera a mostrar la lista pero sin ese numero.

#Actividad 6
lista_saltos = list(range(10, 31, 5))
print(lista_saltos[:2])

#Actividad 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "cronos"
autos[2] = "etios"
print(autos)

#Actividad 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#Actividad 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#Actividad 10
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print(lista_anidada)
# La lista resultante es [15, True, [25.5, 57.9, 30.6], False] 