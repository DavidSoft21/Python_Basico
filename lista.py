#una lista es una estructura de datos de varias pocisiones mutables
lista = [2, "juan", 1+7j, 9.5]
lista2 = ["soy la lista 2",1,2,lista]

print(lista2)
print(lista2[3][3])
print(lista2[3][-1])
print(lista2[-1][-1])

print(lista2[0:1],lista2[3][1:2])

#volcar valores de una lista a variables
a,c,b,d = lista
print(a)
print(b)
print(c)

#volcar valores de una lista a tupla
tupla = tuple(lista)
print(tupla)
#tupla[1] = "camilo"


lista = list(tupla)
lista[1] = "camilo"
print(lista)
print(type(lista))

#fusionando listas
lista_final = lista + lista2
print(lista_final)

#cuenta cuentos elemetos coinciden con un determinado argumento
print(lista_final.count(2))
print(lista_final.count(20))

#devuelve el indice de la primera ocurrencia en una lista
print(lista_final.index(9.5))
#devolvera error de modo que no existe ese elemento en ningun indice
#print(tupla_final.index(20))

#añadir elementos a una lista
lista.append("soy un elemnto añadido")
print(lista)

#insertar un elemento en una posicion espeficifica
lista.insert(1,"COLOMBIA")
print(lista)

#extender una lista
lista.extend(["soy","la lista","extendida"])
print(lista)

#eliminar ultimo elemento de una lista
lista.pop()
print(lista)

#eliminar elementos de una lista
lista.remove("soy un elemnto añadido")
print(lista)

#multiplicar una lista 2 veses
print(lista * 2)

#validar la existencia de un elemento en una lista
print(9.5 in lista)

#ordenar una lista
lista_desordenada = [5,8,1,2,10,3]
lista_desordenada.sort()
#lista_desordenada.sort(reverse=True)
#lista_desordenada.reverse()
print(lista_desordenada)

#nueva_lista_ordenada = sorted(lista_desordenada)
#nueva_lista_ordenada = sorted(lista_desordenada, reverse=True)
#print(nueva_lista_ordenada)

