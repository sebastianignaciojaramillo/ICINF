nombres=[]

for _ in range(7):
    nombre = input("ingrese un nombre: ")
    nombres.append(nombre)

nombres_filtrados = [nombre for nombre in nombres if nombre[-1] != 'a']

print("lista de nombres despues de eliminar los que terminan en 'a': ")
print(nombres_filtrados)
