

import random


def crearCursos(num):
    curso =[] 
    curso = [[]]* num
    return curso

def agregarCursoNombre (lista): 
    for a in range(len(lista)): 
        lista.append(f'curso{a+1}')

def agregarAlumnos(lista, num):
    for item in lista: 
        for i in range(num): 
            item[f'Estudiandte{i}'].append(random.randint(1, 10))



num = int(input('Introduzca el número de cursos a cargar: \n'))
cursos = crearCursos(num)
agregarCursoNombre(cursos)

for curs in cursos:
    print(str(curs))

agregarAlumnos(cursos, 4)

for curs in cursos: 
    for key,value in curs.item: 
        print(f' {curs} + {key} + {value}')


## 2do intento :

import random

#función para crear dictionary curso nuevo
def crearCursos(num):
    cursos =[] 
    for a in range(num):
        cursos[f'curso{a+1}'].append([])    
    return cursos

#función para crear el curso como 
def agregarAlumnos(lista, num):
   for curso in cursos:
        for i in range(num):
            curso[f'alumno{num+1}'].append({'nota': random.randint(1, 10)})
 


num = int(input('Introduzca el número de cursos a cargar: \n'))
cursos = crearCursos(num)

for curs in cursos:
    print(str(curs))

agregarAlumnos(cursos, 4)

for curs in cursos: 
    for key,value in curs.item: 
        print(f' {curs} + {key} + {value}')
