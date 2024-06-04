def contar_vocales_consonantes(palabra):
    lista_vocales = "aeiouAEIOU"
    contador_vocales = 0
    contador_consonantes = 0

    for letra in palabra:
        if letra.isalpha():
            if letra in lista_vocales:
                contador_vocales += 1
            else:
                contador_consonantes += 1

    return contador_vocales, contador_consonantes

def main():
    lista_palabras = []

    while True:
        palabra = input("Ingresa una palabra (o presiona enter para finalizar): ")
        if not palabra:
            break
        lista_palabras.append(palabra)

    for palabra in lista_palabras:
        vocales, consonantes = contar_vocales_consonantes(palabra)
        print(f"Palabra: {palabra}, Vocales: {vocales}, Consonantes: {consonantes}")

if __name__ == "__main__":
    main()
