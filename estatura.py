alturas = 0
sumalturas = 0
cont = 0

while alturas >= 0:
    alturas = float(input("ingrese las alturas de las personas deseadas (0 para terminar): "))
    if alturas == 0:
       break 
    sumalturas= sumalturas + alturas
    cont = cont + 1 

promedio= sumalturas / cont
print("el promedio de estatura es de :", promedio) 

