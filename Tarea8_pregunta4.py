def sumatoria(numero):
    if numero <= 1:
        return numero
    else:
        return numero + sumatoria (numero - 1)
resultado = sumatoria (5)
print("La sumatoria de 5 es:", resultado)