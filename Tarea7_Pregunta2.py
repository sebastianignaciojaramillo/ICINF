vocablos = []

while True:
    vocablo = input("Ingrese una palabra (o presione Enter para finalizar): ")
    if vocablo == "":
        break
    vocablos.append(vocablo)

def contar_a(vocablo):
    return vocablo.count('A') + vocablo.count('a')

print("Conteo de letras 'A' y 'a' en cada palabra:")
for vocablo in vocablos:
    cantidad_a = contar_a(vocablo)
    print("El vocablo ", vocablo, "tiene", cantidad_a, "letras 'A' o 'a'.")
