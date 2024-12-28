numeros = []
print("Ingrese numeros enteros. [-1 para finalizar]: ")

# Bucle while para pedir los valores al usuario.
while True:
    valor = int(input("Ingresa un entero: "))
    if valor == -1:
        break
    
    numeros.append(valor)

# Crear una nueva lista que contenga solo los pares
numeros_pares = []
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)

# Mostrar la lista de numeros pares:
print("-"*25)
print("La lista de numeros pares es:")
print(numeros_pares)