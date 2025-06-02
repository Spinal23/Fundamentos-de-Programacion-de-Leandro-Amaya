'''
Clase:        Clase 6
Tema:         Manejo de listas
Ejercicio:    6.3.1 Numeros Lideres
Descripción:  Definición del ejercicio

Autor:        Nombre del estudiante
Fecha:        2025-05-2
Estado:       [ En progreso]
'''


sec = input("Ingrese números enteros separados por espacios: ") 
sec2 = list(map(int, sec.split()))
sec2.sort(reverse=True)
print("El numero mayor es:",sec2[0])