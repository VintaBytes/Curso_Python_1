# Escribe un programa en Python que 
# solicite al usuario una cadena de 
# texto y cuente cuántas vocales 
# contiene (tanto mayúsculas como 
# minúsculas). 

texto = input("Cadena: ").lower()
print(texto)

cuenta = 0 
for letra in texto:
    if letra in "aeiou":
        cuenta +=1

print("Hay",cuenta, "vocales.")


