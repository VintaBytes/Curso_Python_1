# Pedir la edad de una persona y validarla
# La edad esperada está entre 18 y 45

bandera = True

while bandera: # bandera == True:
    edad = int(input("Ingrese su edad [18..45]: "))
    if edad < 18 or edad > 45:
        print("Error. Intente nuevamente.")
    else:
        bandera = False

print("+++ END +++")