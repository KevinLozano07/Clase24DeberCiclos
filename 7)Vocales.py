#Modifica el código para que también cuente las vocales con acentos (á, é, í, ó, ú).

frase = "Hola, ¿cómo estás?"
vocales = "aeiouáéíóúAEIOU"
contador_vocales = 0
for letra in frase:
 if letra in vocales:
   contador_vocales += 1

print("")
print("El número de vocales es:", contador_vocales)
print("")