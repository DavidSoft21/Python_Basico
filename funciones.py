"""
Las funciones son una agrupacion de sentencias que
nos permite reutilizar codigo a lo largo de la ejecucion
de un programa bajo la palabra reservada def
"""

def saludar(nombre,veses)->str:
    for i in range(veses):
        print(f'Hola, {nombre}!')

nombre = input('Ingrese Nombre: ')
veses = int(input('Ingrese numero de repeticiones: '))

saludar(nombre,veses)

