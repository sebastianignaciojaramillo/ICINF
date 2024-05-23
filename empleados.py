empleados_rango_bajo = empleados_rango_alto = gasto_total = 0

print("Ingrese los sueldos de los empleados mensualmente. Para terminar, ingrese -1.")
      
sueldo = int(input("ingrese el sueldo del empleado (en pesos): "))
while sueldo != -1:
    if sueldo <= 900000:
       empleados_rango_bajo += 1
    else:
       empleados_rango_alto += 1
    gasto_total += sueldo
    sueldo = int(input("ingrese el sueldo del empleado (en pesos): "))

print("Empleados que cobran hasta $900.000: " + str(empleados_rango_bajo))  
print("Empleados que cobran mas de $900.000: " + str(empleados_rango_alto))
print("gasto total en sueldos: $" + str(gasto_total))   