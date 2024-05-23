total_preguntas = int(input("ingrese el total de preguntas: "))
respuestas_correctas = int(input("ingrese la cantidad de respuestas correctas: "))

porcentaje = (respuestas_correctas / total_preguntas) * 100

if porcentaje >= 95:
    nivel = "nivel maximo"
else:
    if porcentaje >= 70:
        nivel = "nivel medio"
    else:
        if porcentaje >= 40:
            nivel = "nivel regular"
        else:
            nivel = "fuera de nivel"

porcentaje_str = str(int(porcentaje * 100) / 100.0)

print("porcentaje de respuestas correctas: " + porcentaje_str + "%")
print("nivel obtenido: " + nivel)
        