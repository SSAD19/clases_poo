import sqlite3


class Base_Datos: 
    
    def conectar_a_base (self):
        try:
            self.db = sqlite3.connect('empleados.db')
        except Exception as e:
            print("Error al conectar a la base de datos: ", e)
            
    def crearTabla(self, query):
        try:
            self.conectar_a_base()
            self.db.execute(query)
        except Exception as e:
            print("Error al crear la tabla: ", e)
    
    def operacioDataBase(self, query):
        try:
            self.conectar_a_base()
            self.db.execute(query)
            self.db.commit()
        except:
            print("Error al crear el registro")
            self.db.rollback()
        finally:
            self.db.close()
            
class Empleado: 
    def __init__(self, legajo:int, dni:int, nombre:str, apellido:str, area:str) -> None:
        self.id
        self.nro_legajo = legajo
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.area = area
            
def main():
    base = Base_Datos()
   
    query = """CREATE IF NOT EXISTS TABLE empledados (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nro_legajo INTEGER NOT NULL UNIQUE,
            dni INTEGER NOT NULL UNIQUE,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            area TEXT NOT NULL
            )"""
   
    base.crearTabla(query)
    
    def iniciaOperaciones(value:bool) -> int: 
        try:
            return input('''
                Indique el número de la operación que desea realizar: 
                1.Insertar un registro de empleado
                2. Seleccionar un registro 
                3. Seleccionar todos los registros
                4. Modificar el área de un empleado
                5. Eliminar un empleado
                6. Finalizar   
              ''')
            
        except Exception as e:
            print('error', e)
    
    def operacionSeleccionada(num:int): 
        match num:
            case 1:
                ejemplo = Empleado(123,20895421, 'pepito', 'juarez','caba')
                agregarEmpelado(ejemplo)
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6: 
                pass
    
    def agregarEmpelado(Datos:Empleado):
        query = 'INSERT into to empleados values(legajo=? ,dni=? ,nombre=? ,apellido=? ,area=?)',  (Datos.nro_legajo, Datos.dni, Datos.nombre, Datos.apellido, Datos.area)
        base.operacioDataBase(query)

    
    operacion = True
    
    while (operacion == True):
        try: 
            num = int(iniciaOperaciones(True))
            operacionSeleccionada(num)
            operacion = input("¿Desea realizar otra operación? (S/N): ")
            if operacion.upper() == "N":
                operacion = False            
        except ValueError as e:
            print('Error: Debe ingresar un número entero')    
        except Exception as e: 
            print('error', e)
            

''' 
El programa debe solicitar al usuario que ingrese por consola una de las siguientes
opciones:
• Opcion 1 Insertar un registro de empleado.
• Opcion 2 Selecionar un registro de empleado a partir de su numero DNI.
• Opcion 3 Selecionar todos los empleados o los registros de la tabla.
• Opcion 4 Modificar el area de un empleado en función de su numero de legajo.
• Opcion 5 Eliminar un empleado a partir del numero de legajo.
• Opcion 6 Finalizar.
Cada opción se tiene que ingresar por teclado. Cada una de las sentencias que van a
permitir ejecutar cada opción debe estar en una función por separado (salvo la opción
nro 6). Es decir, la opción 1 “insertar un registro de empleado” tiene su propia función.
La conexión a la Base de Datos también debe estar en una función por separado, al
igual que la creación de la tabla es otra función.
Luego de realizar acciones de modificación de datos INSERT DELETE UPDATE se debe
cerrar la conexión.
Notación: ai auto incremental , pk primary key
'''