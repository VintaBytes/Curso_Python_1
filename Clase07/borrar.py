lista = ["Ana","José", "Ana", "Pedro"]

print(lista)
nombre = input("Nombre: ")

if nombre in lista:
    lista.remove(nombre)
else:
    print(nombre,"no está en la lista.")


print(lista)