# Uso de continue

usuario_ok = "Juan"
pass_ok = "1234"

while True:
    usuario = input("Usuario: ")
    if usuario == usuario_ok:
        password = input("Contraseña: ")
        if password == pass_ok:
            print("ADMITIDO!")
            break # Aborta inmediatamente
        else:
            print("Contraseña erronea!")
    else:
        print("Usuario no existe. Intente nuevamente")
        continue
    print("Holaaaaaa!")


print("Programa Finalizado")
