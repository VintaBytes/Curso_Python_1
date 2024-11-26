# calculadora de propinas
cuentaTotal = input("Cuenta total: ")
porcentaje = input("Porcentaje  : ")

cuentaTotal = float(cuentaTotal) # 100.0
porcentaje = int(porcentaje)

propina = cuentaTotal * porcentaje / 100

print("La propina es de", propina)