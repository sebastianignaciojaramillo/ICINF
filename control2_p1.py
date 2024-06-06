puntajes = []


for i in range(1, 16):
    while True:
        puntaje = int(input(f"ingrese el puntaje del dia {i} (entre 1 y 100): "))
        if 1 <= puntaje <= 100:
            puntajes.append(puntaje)
            break
        else:
            print("el puntaje debe estar entre 1 y 100. Intente de nuevo.")

dias_mayor_igual_60=[]
dias_menor_60=[]

for i in range(len(puntajes)):
    if puntajes[i] >= 60:
        dias_mayor_igual_60.append(f"dia {i + 1}")
    else:
        dias_mayor_igual_60.append(f"dia {i+1}")
        
print("dias con puntaje mayor o igual a 60 puntos:")
print(dias_mayor_igual_60)

print("dias con puntaje menor a 60 puntos:")
print(dias_menor_60)
