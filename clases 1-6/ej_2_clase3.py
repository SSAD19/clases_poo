#Usando la función del ejercicio anterior, escribir un programa que pida al usuario dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y muestre por pantalla la duración total en horas, minutos y segundos.

def calcularSegundos(horas, minu, seg): 
    segHor = horas * 3600
    segMin = minu * 60
    total = segHor + segMin + seg  
    return total

def sumarVarios (*otros): 
    total = 0
    for otro in otros:
        total += otro
    return total 
        

print('Ahora se calculara el total de segundos en dos dos intervalos de horarios diferentes, para mostrat los segundos totales.')
hor = int(input('introduzca la hora en formato 12 horas: \n Ej. :(08): '))
minu = int(input('introduzca los minutos: \n Ej. : (45): '))
segs = int(input('introduzca los segundos: \n Ej. : (19): '))

totalSegundos1= calcularSegundos(hor,minu,segs)

print('Introdusca los datos del segundo intérvalo según se solciita:')
hor2 = int(input('introduzca la hora en formato 12 horas: \n Ej. :(08): '))
minu2 = int(input('introduzca los minutos: \n Ej. : (45): '))
segs2 = int(input('introduzca los segundos: \n Ej. : (19): '))

totalSegundos2= calcularSegundos(hor2,minu2,segs2)

totalFinal = sumarVarios(totalSegundos1, totalSegundos2)

print(f'El total de segundos en el horario exacto proporcionado es de : {totalFinal}')