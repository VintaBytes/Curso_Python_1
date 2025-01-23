lista = [ -30, 6, 1, 9 , 12, -3]


minimo = lista[0]
maximo = lista[0]

for numero in lista:
    if numero < minimo:
        minimo = numero
    if numero > maximo:
        maximo = numero

print("El mínimo es:", minimo)
print("El maximo es:", maximo)
