'''
Clase:        Clase 5
Tema:         Loops 
Ejercicio:    Ejercicio 5.4.2
Descripción:  Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito. Ejemplo:
Si el usuario ingresa 9875, entonces: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2

Autor:        Leandro Amaya
Fecha:        2025-05-29
Estado:       [ Terminado ]
'''

from functools import reduce

num = input("Ingrese un numero ENTERO ")

num1 = list(map(int,num))
def reducir(x, y):
  return x + y

while True:
    res = reduce(reducir, num1)
    unir = ''.join(map(str, num1))
    print(f"{unir} = {res}")
    
    if res < 10:
        print(f"Resultado final : {res}")
        break
    else:
        num1 = list(map(int, str(res)))
