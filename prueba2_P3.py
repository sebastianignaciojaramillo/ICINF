turistas = {}

for x in range(5):
    nombre = input("Ingrese el nombre del turista: ")
    pais = input("Ingrese el pais de procedencia del turista: ")
    turistas[nombre] = pais

nombre_turista = input("Ingrese el nombre de uno de los turistas previamente ingresados: ")

if nombre_turista in turistas:
    print("El turista con el nombre " + nombre_turista + " viene del pais " + turistas[nombre_turista])
else:
    print ("El turista con el nombre " + nombre_turista + " no se encuentra en el registro.")  
