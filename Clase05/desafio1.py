# Desafío 1: 
# Escribe un programa que pida el nombre del usuario.
# Si el nombre es una cadena vacía, volver a pedirlo
# hasta que se ingrese un nombre válido.

nombre = ""

# Bucle while que se ejecuta mientras la cadena esté vacía
while not nombre.strip():
    nombre = input("Por favor, ingresa tu nombre: ")
    if not nombre:
        print("El nombre no puede estar vacío. Inténtalo de nuevo.")

print("¡Hola,", nombre, "! Bienvenido.")