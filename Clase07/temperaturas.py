temperaturas = []

print('Ingrese las temperaturas. "FIN" para salir')
print()
while True:
    temp = input("Temperatura: ")
    if temp.upper().strip()=="FIN":  #fin, FIn => FIN
        break
    else:
        temperaturas.append(float(temp))

# Calcular el promedio
cantidad = len(temperaturas)
suma_de_temperaturas = 0

for temperatura in temperaturas:
    suma_de_temperaturas += temperatura

promedio = suma_de_temperaturas / cantidad

# Mostramos el resultado
print("La temperatura promedio es de:",promedio, "grados." )