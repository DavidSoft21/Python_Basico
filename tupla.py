#una tupla es una estructura de datos de varias pocisiones no mutables
tupla = 2, "juan", 1+7j, 9.5
tupla2 = "soy la tupla 2",1,2,tupla

print(tupla2)
print(tupla2[3][3])
print(tupla2[3][-1])
print(tupla2[-1][-1])

print(tupla2[0:1],tupla2[3][1:2])
#marcara una traza debido a queno soporta asignaciones porque es un objeto inmutable
#tupla[1] = "camilo"

#volcar valores de una tupla a variables
a,c,b,d = tupla
print(a)
print(b)
print(c)

#volcar valores de una tupla a listas
lista = list(tupla)
print(lista)
lista[1] = "camilo"
print(lista)

tupla = tuple(lista)
print(tupla)
print(type(tupla))

#fusionando tuplas
tupla_final = tupla + tupla2
print(tupla_final)

#cuenta cuentos elemetos coinciden con un determinado argumento
print(tupla_final.count(2))
print(tupla_final.count(20))

#devuelve el indice de la primera ocurrencia en una tupla
print(tupla_final.index(9.5))
#devolvera error de modo que no existe ese elemento en ningun indice
#print(tupla_final.index(20))

#multiplicar una tupla 2 veses
print(tupla * 2)

#validar la existencia de un elemento en una tupla
print(2.0 in tupla)

#ordenar una tupla
tupla = 1,5,8,3,2
#tupla_ordenada = tuple(sorted(tupla))
tupla_ordenada = tuple(sorted(tupla,reverse=True))
print(tupla_ordenada)
