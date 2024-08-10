#Modifica el código para generar la tabla de multiplicar del número que el usuario elija.

print("")
numero = int(input("Ingrese un numero: "))
i = 1

print("")
while i <= 10:
 print(f"{numero} x {i} = {numero * i}")
 i += 1
print("")