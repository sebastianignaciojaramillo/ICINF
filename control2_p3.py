palabras=[]

while True:
    palabra=input("ingrese una palabra (o presione enter para finalizar): ")
    if palabra == "":
     break
    palabras.append(palabra)
if palabras:
   max_lenght = max(len(p)for p in palabras)
   print("la longitud de la palabra con mayor caracteres es de : ", max_lenght)
else:
   print("no se ingresaron palabras.")
          


