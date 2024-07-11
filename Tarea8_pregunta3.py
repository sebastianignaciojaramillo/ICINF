def separar(lista):
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return sorted(pares), sorted(impares)
     
lista = [6, 5, 2, 1, 7]
pares, impares = separar(lista)
print(pares)
