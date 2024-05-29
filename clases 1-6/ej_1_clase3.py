#Escribir una función que permita calcular la duración en segundos de un intervalo dado en horas, minutos y segundos.

def calcularSegundos(horas, minu, seg): 
    segHor = horas * 3600
    segMin = minu * 60
    total = segHor + segMin + seg  
    return total


hor = int(input('introduzca la hora en formato 12 horas: \n Ej. :(08): '))
minu = int(input('introduzca los minutos: \n Ej. : (45): '))
segs = int(input('introduzca los segundos: \n Ej. : (19): '))

totalSegundos= calcularSegundos(hor,minu,segs)
print(f'El total de segundos en el horario exacto proporcionado es de : {totalSegundos}')