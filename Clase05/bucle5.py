# Pedir la edad de una persona y validarla
# La edad esperada está entre 18 y 45



while True: # Siempre va a ser verdadero!!!
    edad = int(input("Ingrese su edad [18..45]: "))
    if edad < 18 or edad > 45:
        print("Error. Intente nuevamente.")
    else:
        break # Aborta inmediatamente
    

print("+++ END +++")