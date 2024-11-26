# calculadora de propinas
cuentaTotal = float(input("Cuenta total: "))
porcentaje = int(input("Porcentaje  : "))

propina = cuentaTotal * porcentaje / 100

print("La propina es de " + str(propina))
