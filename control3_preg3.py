def potencia(num, exp):
    if exp == 0:
        return 1
    elif exp > 0:
        return num * potencia(num, exp -1)
    else:
        return 1 / potencia(num, -exp)
    
print (potencia(3, 3))
print(potencia(5, 2))
print(potencia(2, 6))