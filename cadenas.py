texto = "este ES el aRchivo de manejo de cadenas"
# lower - upper - title - find - count -  replace - isnumeric - split
#Imprime un texto
print(texto)
#Imprime un texto minusculaS
print(texto.lower())
#Imprime un texto mayusculas
print(texto.upper())
#Imprime un texto capitalice
print(texto.title())
#Imprime posicion donde comienza una frase
print(texto.find("de"))
#Imprime cuantas veses se repite una frase
print(texto.count("de"))
#reemplaza texto por otro
texto_final = texto.replace("aRchivo","nuevo texto")
print(texto_final)
#Imprime true cuando el texto es un numero
numero = "105"
print(numero.isnumeric())
#separa en elementos de un arreglo un valor existente en la cadena para dividirla
print(texto.split(" "))
