#Escribir una función que reciba una muestra de números en una lista y retorne su media.

import random


def calcularMedia(lista): 
    total = 0
    for num in lista:
        total +=num
    media = total/len(lista)
    return media

listaNum = [random.randint(1, 15) for _ in range(10)]

media = calcularMedia(listaNum)
print(listaNum, ' ', media)


