puntajes = []

while True:
    puntaje = float(input("ingrese un puntaje PAES(o ingrese 0 para finalizar): "))
    if puntaje == 0:
        break
    puntajes.append(puntaje)

if puntajes:
    promedio = sum(puntajes) / len(puntajes)
    puntaje_bajo = min(puntajes)
    puntaje_alto = max(puntajes)

    print("Promedio de los puntajes PAES ingresados:", promedio)
    print("Puntaje PAES menor ingresado:", puntaje_bajo)
    print("Puntaje PAES mayor ingresado:", puntaje_alto)
    
else:
    print("No se ingresaron puntajes. ")    

    