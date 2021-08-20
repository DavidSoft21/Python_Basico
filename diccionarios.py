"""
Los diccionarios son estructuras de datos de varias posiciones dinamicas y mutables
organizados por clave y valor que nos permiten almacenar diferentes tipos de valores
"""

#Declarando Dict
paises = {"EE.UU": "Whashintong","Colombia": "Bogota", "Peru":"Lima"}
print(paises)
#print(paises["EE.UU"])


#agregando elementos a un diccionario
paises["Venezuela"]="Caracas"
print(paises)
#Reemplazar elementos a un diccionario
paises["Venezuela"]="Tachira"
print(paises)

#eliminar elementos de un diccionario
del paises["Venezuela"]
print(paises)

#datos en los dict
dict2 = {25:True, "complejo":52j, 10.5:5}
print(dict2)

key = "EE.UU","COLOMBIA","VENEZUELA"
Values = ["Whashintog","Bogota","Caracas"]
paises_mundo = {key[0]:Values[0],key[1]:Values[1],key[2]:Values[2]}
print(paises_mundo)

#obtener valores con metodo get por medio de llaves
print(paises_mundo.get("EE.UU","Estados Unidos"))
print(paises_mundo.get("EE.U","Estados Unidos"))

#obtener todas las llaves de un dict
print(paises_mundo.keys())

#obtener todas los valores de un dict
print(paises_mundo.values())

#obtener tuplas por elementos del dict
print(paises_mundo.items())

#ordenar elementos de un diccionario en una lista
paises_ordenados = sorted(paises.keys(), reverse=True)
print(paises_ordenados)

paises_ordenados = sorted(paises.values())
print(paises_ordenados)

paises_ordenados = sorted(paises.items())
print(paises_ordenados)



