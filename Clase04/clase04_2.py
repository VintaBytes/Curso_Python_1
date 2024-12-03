# determine si una persona es mayor de edad,
# Validando que tenga menos de 70 años.
edad = int(input("Edad: "))

if edad < 70:
    if edad >= 18:
        print("La persona es MAYOR de edad.")
    else:
        print("La persona es MENOR de edad.")
else:
    print("Las edades válidas son menores a 70 años.")
