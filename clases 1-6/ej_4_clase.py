#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

import random

def calcularCuadrados(lista): 
    total = []
    for num in lista:
        total.append(num * num)
    return total 

listaNum = [random.randint(1, 15) for _ in range(10)]
listaCuadrado = calcularCuadrados(listaNum)

print(listaNum, ' ', listaCuadrado )
