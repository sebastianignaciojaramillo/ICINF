inventario = {}

while True:
    item = input("Ingrese el nombre del producto (o presione Enter para finalizar): ")
    if item == "":
        break
    cantidad = int(input(f"Ingrese la cantidad de {item}: "))
    inventario[item] = cantidad

x = int(input("Ingrese un valor numérico X para multiplicar las cantidades: "))

print("Productos y sus cantidades multiplicadas por X:")
for item, cantidad in inventario.items():
    print(item, ":", cantidad * x)
