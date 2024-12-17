# Solicitar al usuario un número entero
N = int(input("Ingrese un número entero: "))

# Inicializar la variable para la suma
suma = 0

# Sumar todos los números desde 1 hasta N
for num in range(1, N + 1):
    suma += num

# Mostrar el resultado
print("La suma de los números del 1 al", N, "es:", suma)