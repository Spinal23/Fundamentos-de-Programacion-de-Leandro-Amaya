'''
Clase:        Clase 6
Tema:         Listas
Ejercicio:    Eliminando Valores duplicados
Descripción:  Dada una lista ingresada por el usuario, elimina los elementos duplicados manteniendo la primera aparicion de cada numero

Autor:        Leandro Amaya
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''
#Lo volvi a subir desde git, puesto que antes lo habia subido en la interfaz web
lista = list(input("Escribe la serie de datos deseados").split(" "))
vacia = []
for ola in lista:
  if ola not in vacia:
    vacia.append(ola)
    print(ola, end = " ")