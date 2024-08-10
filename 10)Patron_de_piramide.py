 #Deber: Modifica el código para que la pirámide tenga una altura que el usuario pueda elegir.

print("")
n = int(input("Ingrese un numero: "))

print("")
for i in range(1, n + 1):
 print(" " * (n - i) + "*" * (2 * i - 1))
print("")