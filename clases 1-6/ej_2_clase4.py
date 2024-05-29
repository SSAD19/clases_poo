'''
Crear una clase llamada ListaDeTareas con los siguientes atributos y métodos:
• Atributo de instancia privado “lista_tareas” de tipo list.
• Método de instancia público “agregarTarea(tarea)”, que recibe como argumento
una tarea que debe ser agregada a la lista de tareas (atributo “lista_tareas”) y
retorna el string “Tarea agregada correctamente a la lista” ó “La tarea no fue
agregada a la lista” en caso que la tarea se haya agregado o no a la lista
respectivamente.
• Método de instancia público “quitarTarea(tarea)”, que recibe como argumento una
tarea que debe ser eliminada de la lista de tareas (atributo “lista_tareas”) y retorna
el string “Tarea eliminada correctamente de la lista” ó “La tarea no fue eliminada de
la lista” en caso que la tarea se haya eliminado o no de la lista respectivamente.
• Método de instancia público “mostrarTareas()”, que no recibe ningún argumento y
retorna la lista de tareas (atributo “lista_tareas”) .
Luego, se debe crear una instancia de ListaDeTareas, agregar tareas a la lista, eliminar
tareas de la lista y finalmente imprimir la lista completa de tareas.
Nota: el método “quitarTarea(tarea)” debe validar si la tarea a eliminar existe en la lista
antes de ser eliminada.

'''
class ListaDeTareas: 
    
    __lista_tareas = []
    
    def agregarTareas(self, tarea):
        try:
            if tarea not in self.__lista_tareas:
                self.__lista_tareas.append(tarea)
                print(f'tarea agregada: {tarea}')
            else: 
                print('la tarea ya existe')
        except: 
            print('no se pudo agregar la tarea')
                
    def quitarTareas(self, tarea): 
        try:
            if tarea in self.__lista_tareas:
                self.__lista_tareas.remove(tarea)
                print('se elimino la tarea')
            else: 
                print('no se encontró la tarea a eliminar')
        except : 
            print('error, no se pudo eliminar la tarea')
                    
            
    def mostrarTareas(self): 
        if len(self.__lista_tareas)> 0:
            for tarea in self.__lista_tareas: 
                print (tarea)
        else: 
            print('no hay tareas para mostrar')
        

misPendientes = ListaDeTareas()

misPendientes.agregarTareas('Ir al gimnasio')
misPendientes.agregarTareas('Hacer el almuerzo')
misPendientes.agregarTareas('Pasear los perros')
misPendientes.agregarTareas('Ir al banco')

misPendientes.mostrarTareas()

print('Elimino una de las tareas acá')

misPendientes.quitarTareas('Ir al banco')
misPendientes.quitarTareas('eliminar otra cosa1')

misPendientes.mostrarTareas()