'''
Clase:        Clase 7
Tema:         Manejo de matrices 
Ejercicio:    Ejercicio 10.2.1
Descripción:  
Dada una matriz binaria ingresada por el
usuario, verifica para cada celda de una
matriz binaria cuántos elementos con valor
de 1 hay en las celdas vecinas (arriba, abajo,
izquierda, derecha, diagonales).
Entrada:
• Dos números N,M con la dimensión de la
matriz. N conjuntos de M cantidad de
números enteros separados por coma.
Salida:
• Matriz NxM. Cada celda contiene la suma
de elementos con valor de 1 en las celdas
vecinas .

Autor:        Leandro Amaya
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''

N = int(input("Ingrese la cantidad de filas (N): "))
M = int(input("Ingrese la cantidad de columnas (M): "))

matriz = []
for i in range(N):
    while True:
        fila = input(f"Ingrese la fila {i+1} con {M} números separados por coma: ")
        elementos = list(map(int, fila.split(",")))
        if len(elementos) != M:
            print(f"Debe ingresar exactamente {M} números.")
        else:
            matriz.append(elementos)
            break

vecinos = []
for i in range(N):
    fila = []
    for j in range(M):
        fila.append(0)
    vecinos.append(fila)

for i in range (N):
  for j in range(M):
    suma=0
    for fila in range(i-1,i+2):
      for colum in range(j-1,j+2):
        if 0 <= fila < N and 0 <= colum <M:
          if fila== i and colum ==j:
            continue
          if matriz[fila][colum] == 1:
            suma += 1
    vecinos[i][j] = suma

print("\nMatriz original:")
for fila in matriz:
    print(fila)

print("\nMatriz de conteo de vecinos con valor 1:")
for fila in vecinos:
    print(fila)
