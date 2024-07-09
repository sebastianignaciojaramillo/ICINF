lista_euros = []
euro_a_clp = 1011

for _ in range (5):
    producto = float(input("Ingrese el precio de un producto en euros: "))
    lista_euros.append(producto)

lista_clp = [producto * euro_a_clp for producto in lista_euros]

print("Los precios en pesos chilenos son:", lista_clp)
    