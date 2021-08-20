#python es case sensitive

Nombre = "David"

nombre = "david"

if Nombre != nombre:
    print("son diferentes")

#tipado dinamico
numeros = "25"

print(type(numeros))

numeros = 25

print(type(numeros))

#permite asignacion multiple

var1, var2, var3 = 25, 50, 75

#formas de imprimir
print("var1 = {} var2 = {} var3 = {}".format(var1, var2, var3))
print(f"var1 = {var1} var2 = {var2} var3 = {var3}")
print("var1 =",var1,"var2 =",var2,"var3 =",var3)
print("var1 =",var1,"\nvar2 =",var2,"\nvar3 =",var3)
print("var1 =",var1,"\tvar2 =",var2,"\tvar3 =",var3)

num1, num2 = "5","3"
print(num1+num2)
print(float(int(num1)+2))
print(num1+str(2))
#Marcara error ya que no podemos operar variables de str con int
print(num1+2)


