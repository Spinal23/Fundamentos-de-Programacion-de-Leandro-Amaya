'''
Clase:        Clase 7
Tema:         Manejo de matrices 
Ejercicio:    Ejercicio 10.3.1
Descripción:  
Dada una matriz cuadrada ingresada por el
usuario, comprueba si la matriz cuadrada es
simétrica respecto a su diagonal principal.
Entrada:
• Numero entero N con la dimensión de la
matriz. N conjuntos de números enteros
separados por coma.
Salida:
• Una línea con una cadena de texto. “La
matriz es simétrica” si es simétrica; “La
matriz no es simétrica” en caso contrario.
Autor:        Leandro Amaya
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''


N = int(input("Ingrese la cantidad de filas que quiere ingresar (N): ")) 
#Deje las dimensiones de la matriz puesto que al intentar de otra forma, el codigo pedia filas de forma perpetua.
matriz = []
for i in range(N):
    fila = input(f"Ingrese la fila {i+1} (números separados por coma): ")
    elementos = list(map(int, fila.split(",")))
    matriz.append(elementos)

simetrica = True
for i in range(N):
    for j in range(N):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break
    if not simetrica:
        break

if simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")