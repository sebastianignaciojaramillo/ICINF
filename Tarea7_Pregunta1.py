numbers = []

for i in range(10):
    number = int(input("Ingrese 10 numeros: "))
    numbers.append(number)
numbers.reverse()

print("Los números en orden inverso son:")
for number in numbers:
    print(number)