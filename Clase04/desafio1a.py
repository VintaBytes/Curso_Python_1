saldo = 100
monto = float(input("Monto a retirar: "))

if monto <= 200:
    if saldo >= monto:
        print("Monto retirado:", monto)
    else:
        print("Saldo insuficiente.")
        print("SALDO:", saldo)
else:
    print("No es posible retirar mas de $ 200")