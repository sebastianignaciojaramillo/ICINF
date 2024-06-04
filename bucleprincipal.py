def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Ingresar un elemento a la lista")
    print("2. Modificar un elemento de la lista según el índice")
    print("3. Eliminar un elemento de la lista según el índice")
    print("4. Eliminar el último elemento de la lista")
    print("5. Buscar un elemento de la lista según el dato (devuelve el índice)")
    print("6. Mostrar todos los elementos de la lista")
    print("7. Salir")

def ingresar_elemento(lista):
    elemento = input("Ingrese el elemento a agregar: ")
    lista.append(elemento)
    print(f"Elemento '{elemento}' agregado a la lista.")

def modificar_elemento(lista):
    try:
        indice = int(input("Ingrese el índice del elemento a modificar: "))
        if 0 <= indice < len(lista):
            nuevo_elemento = input("Ingrese el nuevo valor del elemento: ")
            lista[indice] = nuevo_elemento
            print(f"Elemento en el índice {indice} modificado.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Por favor, ingrese un número válido para el índice.")

def eliminar_elemento(lista):
    try:
        indice = int(input("Ingrese el índice del elemento a eliminar: "))
        if 0 <= indice < len(lista):
            eliminado = lista.pop(indice)
            print(f"Elemento '{eliminado}' eliminado de la lista.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Por favor, ingrese un número válido para el índice.")

def eliminar_ultimo_elemento(lista):
    if lista:
        eliminado = lista.pop()
        print(f"Último elemento '{eliminado}' eliminado de la lista.")
    else:
        print("La lista está vacía.")

def buscar_elemento(lista):
    elemento = input("Ingrese el elemento a buscar: ")
    if elemento in lista:
        indice = lista.index(elemento)
        print(f"El elemento '{elemento}' se encuentra en el índice {indice}.")
    else:
        print(f"El elemento '{elemento}' no se encuentra en la lista.")

def mostrar_lista(lista):
    if lista:
        print("Elementos de la lista:")
        for i, elemento in enumerate(lista):
            print(f"{i}: {elemento}")
    else:
        print("La lista está vacía.")

def main():
    lista = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ingresar_elemento(lista)
        elif opcion == '2':
            modificar_elemento(lista)
        elif opcion == '3':
            eliminar_elemento(lista)
        elif opcion == '4':
            eliminar_ultimo_elemento(lista)
        elif opcion == '5':
            buscar_elemento(lista)
        elif opcion == '6':
            mostrar_lista(lista)
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()