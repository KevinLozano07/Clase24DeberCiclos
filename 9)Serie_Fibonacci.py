#Deber: Modifica el código para que el usuario elija cuántos términos de la serie desea ver.

print("")
n = int(input("Ingrese el valor: "))

a, b = 0, 1
contador = 0

print("")
while contador < n:
 print(a)
 a, b = b, a + b
 contador += 1
print("")