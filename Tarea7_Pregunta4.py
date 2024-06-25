clientes = {}

print("Ingrese el RUT y la deuda de 5 personas:")
for _ in range(5):
    rut = input("Ingrese el RUT: ")
    deuda = int(input("Ingrese la deuda en pesos: "))
    clientes[rut] = deuda

print("Ingrese el RUT de la persona y el monto del abono. Para finalizar, presione Enter sin ingresar un RUT.")
while True:
    rut = input("Ingrese el RUT de la persona: ")
    if rut == "":
        break
    if rut in clientes:
        abono = int(input("Ingrese el monto del abono: "))
        clientes[rut] -= abono
        if clientes[rut] <= 0:
            del clientes[rut]
    else:
        print("El RUT ingresado no está en la lista de clientes.")

print("Personas que quedaron deudoras y sus respectivos saldos de deuda:")
for rut, deuda in clientes.items():
    print("RUT: " + rut + ", Deuda: " + str(deuda))
