# determine si una persona es mayor de edad,
# Validando que tenga menos de 70 años.
# y mas de 0.
edad = int(input("Edad [0..70]: "))

if edad > 0 and edad < 70:
    if edad >= 18:
        print("La persona es MAYOR de edad.")
    else:
        print("La persona es MENOR de edad.")
else:
    print("Las edades deben ser mayores a 0 y menores a 70.")
