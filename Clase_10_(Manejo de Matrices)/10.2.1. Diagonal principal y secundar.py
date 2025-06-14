'''
Clase:        Clase 7
Tema:         Manejo de matrices 
Ejercicio:    Ejercicio 10.2.1
Descripción:  
Dada una matriz cuadrada ingresada por el
usuario, crea dos listas, una con los
elementos de la diagonal principal y la otra
con los elementos de la diagonal
secundaria.
Entrada:
• Numero entero N con la dimensión de la
matriz. N conjuntos de números enteros
separados por coma.
Salida:
• Dos listas, una con los elementos de la
diagonal principal y la otra con los
elementos de la diagonal secundaria.

Autor:        Leandro Amaya
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''
N = int(input("Ingrese la dimensión de la matriz (N): "))

matriz = []
for i in range(N):
    fila = input(f"Ingrese la fila {i+1} (números separados por coma): ")
    elementos = list(map(int, fila.split(",")))
    if len(elementos) != N:
        print("Error: la fila no tiene la cantidad correcta de elementos.")
    matriz.append(elementos)


diag_dom = [matriz[i][i] for i in range(N)]
diag_sec = [matriz[i][N-i-1] for i in range(N)]

print(diag_dom)
print(diag_sec)
