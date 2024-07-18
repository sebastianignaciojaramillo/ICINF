def convierte_negativo(lista):
    return [-num for num in lista]
def solicitar_numeros():
    lista_numeros = []
    for i in range(10):
        num = int(input("introduce el numero positivo " + str(i+1) + ": "))
        lista_numeros.append(num)
    return lista_numeros

lista_numeros = solicitar_numeros()
lista_negativos = convierte_negativo(lista_numeros)

print("Lista con los numeros convertidos en negativos: ")
print(lista_negativos)
