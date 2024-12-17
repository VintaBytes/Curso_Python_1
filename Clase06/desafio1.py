# Solicitar al usuario una cadena de texto
cadena = input("Ingrese una cadena de texto: ")

# Inicializar un contador de vocales
contador_vocales = 0

# Recorrer cada carácter de la cadena
for letra in cadena:
    if letra.lower() in "aeiou":
        contador_vocales += 1

# Mostrar el resultado
print("La cantidad de vocales es:", contador_vocales)