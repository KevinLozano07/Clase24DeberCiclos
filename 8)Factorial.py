#Modifica el código para que el usuario pueda ingresar el número del cual desea calcular el factorial.

print("")
numero = int(input("Ingrese el numero del que desea saber su factorial: "))
factorial = 1

for i in range(1, numero + 1):
 factorial *= i

print("")
print(f"El factorial de {numero} es:", factorial)
print("")
