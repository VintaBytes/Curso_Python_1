# Desafío 2:
# Escribe un programa que pida el nombre del usuario
# y su contraseña. Si no son correctos luego de tres
# intentos, mostrar un texto indicando que el acceso
# ha fallado.
# Caso contrario, permitir el acceso al sistema.


# Datos correctos predefinidos
USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "1234"

intentos = 0
max_intentos = 3

# Bucle while para permitir hasta tres intentos
while intentos < max_intentos:
    usuario = input("Ingresa tu nombre de usuario: ")
    contrasena = input("Ingresa tu contraseña: ")

    if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
        print("¡Acceso concedido! Bienvenido al sistema.")
        break
    else:
        intentos += 1
        print("Usuario o contraseña incorrectos. Intento N°", intentos)

# Si se superan los tres intentos
if intentos == max_intentos:
    print("Acceso fallido. Has superado el número máximo de intentos.")
