'''    Crear una clase llamada Persona.
Con los siguientes atributos privados:
•nombre
•edad
•dni
Y los siguientes métodos:
•mostrar_edad(): retorna la edad de la persona
•es_mayor_edad(): retorna True si edad es mayor o igual a 18, o False si es menor a 18.

El método constructor __init__ de la clase debe recibir y asignar los valores a cada uno de
los atributos privados de la clase.'''

class Persona: 
    
   
    
    #getter y setters
    
    def __init__(self, nombre, edad, dni):
          self.__nombre = nombre
          self.__edad = edad
          self.__dni = dni
        
        
    def mostrar_edad(self): 
        print(self.__edad)
        
    def es_mayor_edad(self):           
        if self.__edad > 17 :
            print('Es mayor de edad')
        elif self.__edad < 18 and self.__edad > 0:
            print('Es menor de edad') 
        else: 
            print('La edad es incorrecta')   
    
    
alumno = Persona('Stef', 33, 2563)
alumno.mostrar_edad()
alumno.es_mayor_edad()

alumno = Persona('Pedro', 12, 2564)
alumno.mostrar_edad()
alumno.es_mayor_edad()

alumno = Persona('No existe', 0, 2563)
alumno.mostrar_edad()
alumno.es_mayor_edad()