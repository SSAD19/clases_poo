#Ejercicio 5  

# lista de 10 cursos 
# cada lista debe tener 30 datos (alumno : nota )
# mostrar promedio por curso  Listo .- Listo 
# mostrar curso con mejor promedio general .- listo 
# alumno y curso del mejor promedio individual 

import random


#función para crear cursos deseados 
def crearCursos(num):
    lista = [[]]*num
    return lista
  
#función para crear dictionary con alumnos/notas en cada curso     
def asignarAlumnos (lista, num): 
      for i in range(len(lista)): 
        lista[i] = {}
        for al in range(num):
            nota = random.randint(1, 10)
            name =f'Alumno_{al}'
            lista[i].update({ name: nota})
            
#Funcion para buscar la media de promedio mas alto de los salones           
def sacarPromedios (lista): 
    promedio = 0
    curs = 0
    for i in range(len(lista)):
        if lista[i]:
            prom = sum(lista[i].values())/len(lista[i])
            print(f'Promedio: {prom} curso #{i+1}')
            if prom > promedio:
                promedio = prom
                curs = str(i+1)
    return promedio, curs


#Funcion para mostrar alumno, curso y nota del promedio  general mas alto 
def alumnoProm (lista): 
    nota = 0
    curs = 0
    alumno = ''
    for i in range(len(lista)):
        if lista[i]:
            for name, value in lista[i].items():
                if value > nota:
                    nota = value
                    curs = str(i+1)
                    alumno = name
    return nota, curs, alumno
        
cursos = crearCursos(5)
print(cursos)

asignarAlumnos(cursos,5)

for i in range(len(cursos)):
    print(cursos[i])


MayorProm, cursoProm =sacarPromedios(cursos)
print(f'El Mayor promedio fue {MayorProm} del curso #{cursoProm}.')
promAlumn,  salon, alumn = alumnoProm(cursos)
print(f'y el alumno con mayor nota  fue {alumn} del curso #{salon}, con una nota de {promAlumn}.')









