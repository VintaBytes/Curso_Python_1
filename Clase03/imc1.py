# Pedir datos:
peso = float(input("Su peso [Kg]: "))
estatura = float(input("Estatura [m]: "))

# Calculamos el IMC:
imc = peso / (estatura * estatura)
# imc = peso / estatura ** 2

# Mostramos el IMC:
print("El IMC es de:", round(imc, 0))
