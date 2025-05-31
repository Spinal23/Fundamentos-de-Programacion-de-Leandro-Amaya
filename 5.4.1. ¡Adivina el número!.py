'''
Clase:        Clase 5
Tema:         Loops 
Ejercicio:    Ejercicio 5.4.1
Descripción:  Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
El programa debe seguir pidiendo números hasta que acierte. En cada
intento fallido el programa notificará al usuario si el número secreto es
mayor o menor al último valor ingresado.

Autor:        Leandro Amaya
Fecha:        2025-05-29
Estado:       [ Terminado ]
'''

import random

NumeroR = random.randint(1,100)
encontrado =  False
#imprimo el numero para facilitar la revision del codigo, pero en la vida real el numero a adivinar no deberia mostrarse
print(f"el numero a adivinar es : {NumeroR}")
while encontrado == False:
    a = int(input("Escribe un numero del 1 al 100  "))

    if a < NumeroR :
        print("Incorrecto. El numero ingresado es menor al numero original, intenta de nuevo")
    elif a > NumeroR:
        print("Incorrecto. El numero ingresado es mayor al numero original, intenta de nuevo")
    elif a == NumeroR:
        print("Felicidades! Haz adivinado el numero")
        break
