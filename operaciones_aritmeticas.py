"""
Estas son las diferentes
maneras de realizar operaciones
aritmeticas con python
"""
import math

num1 = False
num2 = True

print(num1 * num2)
print(num1 + num2)

num1,num2 = 23,5

#division entera
print(num1//num2)

#division normal
print(num1/num2)

#division con asignacion
num1 //= num2
print(num1)

#multiplicacion con asignacion
num1 *= 4
print(num1)

#potencia con asignacion
num1 = 5
num1 **= 3
print(num1)
print(math.pow(5,3))

#raiz cuadrada con asignacion
num1 = num1** (2*(1/2))
print(num1)

num1 = 4**(1/2)
print(num1)
print(math.sqrt(4))

#sumas con asignacion

num1 += 5
print(num1)

#restas con asignacion
num1 -= 5
print(num1)

numero_complejo = 5 + 25j
print(numero_complejo)



