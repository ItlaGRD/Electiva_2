# Creacion de Matriz

filas = int(input("Cuantas filas tendra su  matriz? "))
columnas = int(input("Cuantas columnas tendra su matriz? "))

matriz = []

# El primer ciclo for es para la fila 1 
for i in range(filas):
    lista = []  # Esta lista es para llenar la matriz (la matriz esta compuesta por mas listas)
    for elemento in range(columnas): 
        lista.append(int(input(f"Ingrese el valor en la posicion {elemento}: ")))
    matriz.append(lista)
    
# Imprimimos la matriz en orden    
for i in matriz:
    print(i, end=" ") # IMprime la matriz en una linea
    print(i) # Imprime la matriz en su forma

        

